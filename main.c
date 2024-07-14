#include <math.h> 
float s = 0.000041; //instrument factors taken from anushka's document 
float e = 0.99; // emissivity of human 
float VVV = 5.0;
void setup() { 
  // analogReference(INTERNAL); 
    Serial.begin(9600);
  // put your setup code here, to run once:

}

void loop() {  
  int sensorValue = analogRead(A0); // reading data from thermistor   
  float voltage = sensorValue * (VVV / 1023.0); // converting analog values to voltage  
  float r = (voltage * 100) / (3.3 - voltage); // calculating thermistor resistance in kiloohm  
  float ambtemp = 98750 / (25 * log(r / 100) + 3950); // calculating temperature in celsius
 
 int sensorValue2 = analogRead(A1); // reading data from thermopile   
 float voltage2 = sensorValue2 * (VVV / 1023.0); // converting analog values to voltage   
 float tobj = pow((voltage2 / (s * e)) + pow(ambtemp,4) , 1 / 4.0 ); // calculating object temperature




Serial.print("Output thermistor voltage = "); 
Serial.println(voltage);  

Serial.print("Thermistor Resistance in kiloohm = "); 
Serial.println(r); 
 
Serial.print("Ambient Temperature in celsius = "); 
Serial.println(ambtemp);   

 Serial.print("Value of thermistor = ");
Serial.println(sensorValue); 

Serial.print("Output Thermopile Voltage = ");
Serial.println(voltage2); 

Serial.println("=============================================================");
Serial.println("=============================================================");
Serial.println("=============================================================");

Serial.print("Object Temperature in celsius = ");
Serial.println(tobj); 

Serial.print("Value of thermopile = ");
Serial.println(sensorValue2);  

delay(2000);





  // put your main code here, to run repeatedly:

}
