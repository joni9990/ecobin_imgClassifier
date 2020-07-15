char serialData;
int pinR = 5;
int pinB = 11;
#define buttonPin 12
int buttonState = 0; 
int i= 0;
String btn = "SinApretar";
bool terminado = false; 

void setup() {
  // put your setup code here, to run once:
  pinMode(pinR, OUTPUT);
  pinMode(pinB, OUTPUT);
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(115200);
  digitalWrite(pinR,LOW);
  digitalWrite(pinB,LOW);
}

void loop() {
  // put your main code here, to run repeatedly:
   buttonState = digitalRead(buttonPin);
   
   while (i <= 0){
    Serial.println(btn);
    i = 3;
    }
    terminado = true;
    if(Serial.available()>0){
     serialData = Serial.read();
      if(serialData == 'r'){
        digitalWrite(pinR,HIGH);
        digitalWrite(pinB,LOW);
        terminado = true;
      }    
     else if (serialData == 'b'){
        digitalWrite(pinR,LOW);
        digitalWrite(pinB,HIGH);
        terminado = true;
      }     
    }
     while(buttonState == HIGH && btn == "SinApretar"){
      btn = "Apretado";
      Serial.println(btn);
     }
     while(buttonState == LOW && btn == "Apretado"){
      btn = "SinApretar";
      Serial.println(btn);
     }
    
   }
