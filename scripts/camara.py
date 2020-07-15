import cv2

def tomarfoto():
    """
    	En este caso, 0 quiere decir que queremos acceder
    	a la cámara 0. Si hay más cámaras, puedes ir probando
    	con 1, 2, 3...
    """
    cap = cv2.VideoCapture(0)

    leido, frame = cap.read()

    if leido == True:
        cv2.imwrite("./foto.jpg", frame)
        #cv2.imshow('Imagen', frame)
        #cv2.waitKey(0)
        print("Foto tomada correctamente")
    else:
        print("Error al acceder a la cámara")

    """
    	Finalmente liberamos o soltamos la cámara
    """
    cap.release()
    cv2.destroyAllWindows()
