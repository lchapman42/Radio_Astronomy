/*
 * Rui Santos 
 * Complete Project Details https://randomnerdtutorials.com
 */
 
#include <TinyGPS++.h>
#include <SoftwareSerial.h>

static const int RXPin = 4, TXPin = 3;
static const uint32_t GPSBaud = 9600;

// The TinyGPS++ object
TinyGPSPlus gps;

// The serial connection to the GPS device
SoftwareSerial ss(RXPin, TXPin);

void setup(){
  Serial.begin(9600);
  ss.begin(GPSBaud);
}

void loop(){

  // This sketch displays information every time a new sentence is correctly encoded.
  while (ss.available() > 0){
    gps.encode(ss.read());
    if (gps.location.isUpdated()){
      Serial.print("T");
      if (gps.time.hour() < 10) { Serial.print("0"); }
      Serial.print(gps.time.hour());
      if (gps.time.minute() < 10) { Serial.print("0"); }
      Serial.print(gps.time.minute());
      if (gps.time.second() < 10) { Serial.print("0"); }
      Serial.print(gps.time.second());
      Serial.print(gps.time.centisecond());
      Serial.print("P"); 
      Serial.print(gps.location.lat(), 8);
      Serial.print("L"); 
      Serial.print(gps.location.lng(), 8);
      Serial.print("A");
      Serial.println(gps.altitude.meters(), 8);
    }
  }
}
