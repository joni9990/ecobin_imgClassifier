# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import serial
import time
from camara import tomarfoto
from db import update_metal,update_papel, update_basura, update_carton, update_carton, update_vidrio,update_plastico, update_reciclable

import argparse
import sys
import time

import numpy as np
import tensorflow as tf


#conexion con arduino
#arduinoData = serial.Serial('COM3', 115200)


#funcion de reconocimiento de objetos
def reconocer():

    respuestaSensor = 0

    def load_graph(model_file):
      graph = tf.Graph()
      graph_def = tf.compat.v1.GraphDef()

      with open(model_file, "rb") as f:
        graph_def.ParseFromString(f.read())
      with graph.as_default():
        tf.import_graph_def(graph_def)

      return graph

    def read_tensor_from_image_file(file_name, input_height=299, input_width=299,
    				input_mean=0, input_std=255):
      input_name = "file_reader"
      output_name = "normalized"
      file_reader = tf.io.read_file(file_name, input_name)
      if file_name.endswith(".png"):
        image_reader = tf.image.decode_png(file_reader, channels = 3,
                                           name='png_reader')
      elif file_name.endswith(".gif"):
        image_reader = tf.squeeze(tf.image.decode_gif(file_reader,
                                                      name='gif_reader'))
      elif file_name.endswith(".bmp"):
        image_reader = tf.image.decode_bmp(file_reader, name='bmp_reader')
      else:
        image_reader = tf.image.decode_jpeg(file_reader, channels = 3,
                                            name='jpeg_reader')
      float_caster = tf.cast(image_reader, tf.float32)
      dims_expander = tf.expand_dims(float_caster, 0);
      resized = tf.compat.v1.image.resize_bilinear(dims_expander, [input_height, input_width])
      normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
      sess = tf.compat.v1.Session()
      result = sess.run(normalized)

      return result

    def load_labels(label_file):
      label = []
      proto_as_ascii_lines =  tf.io.gfile.GFile(label_file).readlines()
      for l in proto_as_ascii_lines:
        label.append(l.rstrip())
      return label

    if __name__ == "__main__":
      model_file = "tf_files/retrained_graph.pb"
      label_file = "tf_files/retrained_labels.txt"
      input_height = 299
      input_width = 299
      input_mean = 128
      input_std = 128
      input_layer = "Mul"
      output_layer = "final_result"

      parser = argparse.ArgumentParser()
      ##parser.add_argument("--image", help="image to be processed")
      ##parser.add_argument("--graph", help="graph/model to be executed")
      ##parser.add_argument("--labels", help="name of file containing labels")
      parser.add_argument("--input_height", type=int, help="input height")
      parser.add_argument("--input_width", type=int, help="input width")
      parser.add_argument("--input_mean", type=int, help="input mean")
      parser.add_argument("--input_std", type=int, help="input std")
      parser.add_argument("--input_layer", help="name of input layer")
      parser.add_argument("--output_layer", help="name of output layer")
      args = parser.parse_args()

      tomarfoto()

      ##if args.graph:
      model_file = ('./../tf_files/retrained_graph.pb')
      ##if args.image:
      file_name = ('./foto.jpg')
      ##if args.labels:
      label_file = ('./../tf_files/retrained_labels.txt')
      if args.input_height:
        input_height = args.input_height
      if args.input_width:
        input_width = args.input_width
      if args.input_mean:
        input_mean = args.input_mean
      if args.input_std:
        input_std = args.input_std
      if args.input_layer:
        input_layer = args.input_layer
      if args.output_layer:
        output_layer = args.output_layer

      graph = load_graph(model_file)
      t = read_tensor_from_image_file(file_name,
                                      input_height=input_height,
                                      input_width=input_width,
                                      input_mean=input_mean,
                                      input_std=input_std)

      input_name = "import/" + input_layer
      output_name = "import/" + output_layer
      input_operation = graph.get_operation_by_name(input_name);
      output_operation = graph.get_operation_by_name(output_name);



      with tf.compat.v1.Session(graph=graph) as sess:
        start = time.time()
        results = sess.run(output_operation.outputs[0],
                          {input_operation.outputs[0]: t})
        end=time.time()
      results = np.squeeze(results)

      top_k = results.argsort()[-5:][::-1]
      labels = load_labels(label_file)

      print('\nEvaluation time (1-image): {:.3f}s\n'.format(end-start))
      template = "{} (score={:0.5f})"
      out_classes = np.array([])
      count = 0
      for i in top_k:
          classes = (labels[i], results[i])
          out_classes = np.append(out_classes, classes)
          count += 1

      out_classes = out_classes.reshape(count, 2)  

      print(out_classes)

      length = len(out_classes)-1

      clase = out_classes[0,0]

      if(clase == "basura"):        
        tipo = "b" 
        #manda al arduino
        #arduinoData.write(b'b')
        update_basura()
        print("El objeto es: " + clase + " , "+ tipo ) 
      else:
        tipo = "r" 
        #manda al arduino
        #arduinoData.write(b'r')
        update_reciclable()             
        print("El objeto es: " + clase + " , "+ tipo ) 

    if clase == "carton":
        update_carton()
    elif clase == "papel":
        update_papel()
    elif clase == "vidrio":
        update_vidrio()
    elif clase == "plastico":
        update_plastico()
    elif clase == "metal":
        update_metal()

    time.sleep(1)



while True:

  #respuestaSensor = str(arduinoData.readline().decode().strip("\r\n"))
  #print(respuestaSensor)

  #if (respuestaSensor == "Apretado"):
    #reconocer()
  respuestaSensor = input()

  if (respuestaSensor == "si"):
        reconocer()
        

  elif (respuestaSensor == "end"):
        break
