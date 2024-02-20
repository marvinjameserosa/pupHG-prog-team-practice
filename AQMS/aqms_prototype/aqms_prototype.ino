/***************************************************************************
  This is a library for the BME680 gas, humidity, temperature & pressure sensor

  Designed specifically to work with the Adafruit BME680 Breakout
  ----> http://www.adafruit.com/products/3660

  These sensors use I2C or SPI to communicate, 2 or 4 pins are required
  to interface.

  Adafruit invests time and resources providing this open source code,
  please support Adafruit and open-source hardware by purchasing products
  from Adafruit!

  Written by Limor Fried & Kevin Townsend for Adafruit Industries.
  BSD license, all text above must be included in any redistribution
 ***************************************************************************/

#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"
#include "Adafruit_SGP30.h"
#include "U8g2lib.h"

U8G2_ST7567_JLX12864_1_SW_I2C u8g2 (U8G2_R2, SCL, SDA); //[full framebuffer, size = 1024 bytes]

// #define BME_SCK 13
// #define BME_MISO 12
// #define BME_MOSI 11
// #define BME_CS 10

#define SEALEVELPRESSURE_HPA (1013.25)
Adafruit_SGP30 sgp;

Adafruit_BME680 bme; // I2C
// Adafruit_BME680 bme(BME_CS); // hardware SPI
// Adafruit_BME680 bme(BME_CS, BME_MOSI, BME_MISO,  BME_SCK);


uint32_t getAbsoluteHumidity(float temperature, float humidity) {
    // approximation formula from Sensirion SGP30 Driver Integration chapter 3.15
    const float absoluteHumidity = 216.7f * ((humidity / 100.0f) * 6.112f * exp((17.62f * temperature) / (243.12f + temperature)) / (273.15f + temperature)); // [g/m^3]
    const uint32_t absoluteHumidityScaled = static_cast<uint32_t>(1000.0f * absoluteHumidity); // [mg/m^3]
    return absoluteHumidityScaled;
}

void setup() {
  Serial.flush();
  delay(5000);
  u8g2.setI2CAddress(0x3F * 2);
  u8g2.begin();
  u8g2.setContrast(175);


  Serial.begin(9600);
  while (!Serial);
  //Serial.println(F("BME680 and SGP30 test"));

  if (!bme.begin()) {
    //Serial.println("Could not find a valid BME680 sensor, check wiring!");
    while (1);
  }


  if (! sgp.begin()){
   // Serial.println("Sensor not found :(");
    while (1);
  }
  //Serial.print("Found SGP30 serial #");
  //Serial.print(sgp.serialnumber[0], HEX);
  //Serial.print(sgp.serialnumber[1], HEX);
  //Serial.println(sgp.serialnumber[2], HEX);

  // Set up oversampling and filter initialization
  bme.setTemperatureOversampling(BME680_OS_8X);
  bme.setHumidityOversampling(BME680_OS_2X);
  bme.setPressureOversampling(BME680_OS_4X);
  bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
  bme.setGasHeater(320, 150); // 320*C for 150 ms

  Serial.print("Temperature, ");
  Serial.print("Pressure, ");
  Serial.print("Humidity, ");
  Serial.print("Gas, ");
  Serial.print("Altitude, ");
  Serial.print("TVOC, "); 
  Serial.print("eCO2, ");
  Serial.print("Raw_H2, "); 
  Serial.print("Raw_Ethanol ");
  Serial.println("");
}

int counter = 0;


void loop() {
  if (! bme.performReading()) {
    //Serial.println("Failed to perform reading :(");
    return;
  }
  
  Serial.print(bme.temperature);
  Serial.print(", ");
  Serial.print(bme.pressure / 100.0);
  Serial.print(", ");
  Serial.print(bme.humidity);
  Serial.print(", ");
  Serial.print(bme.gas_resistance / 1000.0);
  Serial.print(", ");
  Serial.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
  Serial.print(", ");

if (! sgp.IAQmeasure()) {
    //Serial.println("Measurement failed");
    return;
  }
  
  Serial.print(sgp.TVOC); 
  Serial.print(", ");
  Serial.print(sgp.eCO2); 
  Serial.print(", ");

  if (! sgp.IAQmeasureRaw()) {
    //Serial.println("Raw Measurement failed");
    return;
  }
  
  Serial.print(sgp.rawH2); 
  Serial.print(", ");
  
  Serial.print(sgp.rawEthanol); 

 


  counter++;
  if (counter == 30) {
    counter = 0;

    uint16_t TVOC_base, eCO2_base;
    if (! sgp.getIAQBaseline(&eCO2_base, &TVOC_base)) {
      //Serial.println("Failed to get baseline readings");
      return;
    }
    //Serial.print("****Baseline values: eCO2: 0x"); Serial.print(eCO2_base, HEX);
    //Serial.print(" & TVOC: 0x"); 
    //Serial.println(TVOC_base, HEX);
  }


  Serial.println();



  String temperature;
  temperature=String(bme.temperature);
  String humidity;
  humidity=String(bme.humidity);
    String pressure;
  pressure=String(bme.pressure/100);
    String TVOC;
TVOC=String(sgp.TVOC);
  String eco2;
  eco2=String(sgp.eCO2);

   u8g2.firstPage();
		  do {	// clear the internal memory
  u8g2.setFont(u8g2_font_ncenB08_tr);	// choose a suitable font
u8g2.setCursor(0, 15);
u8g2.print("Temperature: "+temperature + " C");
u8g2.setCursor(0, 25);
u8g2.print("Humidity: "+humidity+" %");
u8g2.setCursor(0, 35);
u8g2.print("Pressure: "+pressure+" hPa");	
u8g2.setCursor(0, 45);
u8g2.print("TVOC: "+TVOC+" ppb");
u8g2.setCursor(0, 55);
u8g2.print("eCO2: "+eco2+" ppm");	// write something to the internal memory
  } while ( u8g2.nextPage() );				// transfer internal memory to the display







  delay(2000);





}