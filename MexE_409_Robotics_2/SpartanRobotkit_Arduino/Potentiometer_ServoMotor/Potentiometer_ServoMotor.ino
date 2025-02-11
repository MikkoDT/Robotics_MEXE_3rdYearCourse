#include <Servo.h>
const int Pot=A3, sPin=4; //Change pins for test
float aRead;
float serPos=0;
Servo sv;
int t=1000;

void setup() {
  // put your setup code here, to run once:
  pinMode(Pot,INPUT);
  pinMode(sPin,OUTPUT);
  sv.attach(sPin);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  aRead = analogRead(Pot);
  serPos = (180./1023.)*aRead;

  sv.write(serPos);

  Serial.print("Position: ");
  Serial.print(serPos);
  Serial.println(" deg");
  Serial.println();
  delay(t);
}