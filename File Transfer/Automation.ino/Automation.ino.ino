// author William Vavrik 1/8/18 @ 21:43:18

#include<Servo.h>
/* NOTES:
 *  the x coordinate is positive to the right and negative left
 *  the y coordinate is negative up and positive down
 */
 Servo x;
 Servo y;
 double xPos;
 double yPos;
void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
Serial.setTimeout(2);
x.attach(3);
y.attach(2);
xPos = 90;
yPos = 80;
x.write(xPos);
y.write(yPos);
pinMode(7,OUTPUT);
digitalWrite(7,LOW);
//laser pin
}

double getX(String coordinate){
  double x = coordinate.substring(0,coordinate.indexOf(",")).toDouble();
  Serial.println("X:"+String(x));
  return -x;
}
int getY(String coordinate){
  double y = coordinate.substring(coordinate.indexOf(",")+1,coordinate.length()).toDouble();
  return y;
}




void loop() {
  //digitalWrite(7,LOW);
  // put your main code here, to run repeatedly:
  if(Serial.available()){
    Serial.println("Serial Available");
    String coordinate =Serial.readString();
    Serial.println("Coordinate:"+coordinate);
    double xDif = getX(coordinate);
    Serial.println("xDiff: "+String(xDif));
    double yDif = getY(coordinate);
    Serial.println("yDiff: "+String(yDif));
    if(xDif<3 and yDif<3){
      digitalWrite(7,HIGH);
    }else{
      digitalWrite(7,LOW);
    }
    Serial.println("xPos: before "+String(xPos));
    if((xPos+xDif)>0 & (xPos+xDif)<180){
      xPos += xDif;
    }
    
    Serial.println("xPos: after "+String(xPos));
    Serial.println("yPos: before "+String(yPos));
    if((yPos+yDif)>50 & (yPos+yDif)<150){
      
       yPos += yDif;
       
    }
    
    Serial.println("yPos: after "+String(yPos));
    x.write(xPos);
    y.write(yPos);
  }
}
