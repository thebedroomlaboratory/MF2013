#include <Adafruit_GFX.h>
#include <Adafruit_PCD8544.h>

// pin 7 - Serial clock out (SCLK)
// pin 6 - Serial data out (DIN)
// pin 5 - Data/Command select (D/C)
// pin 4 - LCD chip select (CS)
// pin 3 - LCD reset (RST)
Adafruit_PCD8544 display = Adafruit_PCD8544(7, 6, 5, 4, 3);
#define NUMFLAKES 10
#define XPOS 0
#define YPOS 1
#define DELTAY 2


#define LOGO16_GLCD_HEIGHT 16
#define LOGO16_GLCD_WIDTH  16

static unsigned char PROGMEM logo16_glcd_bmp[] =
{ B00000000, B11000000,
  B00000001, B11000000,
  B00000001, B11000000,
  B00000011, B11100000,
  B11110011, B11100000,
  B11111110, B11111000,
  B01111110, B11111111,
  B00110011, B10011111,
  B00011111, B11111100,
  B00001101, B01110000,
  B00011011, B10100000,
  B00111111, B11100000,
  B00111111, B11110000,
  B01111100, B11110000,
  B01110000, B01110000,
  B00000000, B00110000 };
  
//TMP36 Pin Variables
int sensorPin = 1; //the analog pin the TMP36's Vout (sense) pin is connected to
                        //the resolution is 10 mV / degree centigrade with a
                        //500 mV offset to allow for negative temperatures
int sensorPin1 = 0;

  const int buttonPin = 9;
  int ledPin = 0;
  int buttonState = 0;
  int lastButtonState = 0;     // previous state of the button
  int temperatureCOUT = 0;
/*
 * setup() - this function runs once when you turn your Arduino on
 * We initialize the serial connection with the computer
 */
void setup()
{
  Serial.begin(9600);  //Start the serial connection with the computer
                       //to view the result open the serial monitor 
  pinMode(8, OUTPUT);
  pinMode(buttonPin, INPUT);  
   
  display.begin();
  display.clearDisplay();
  
  // init done

  // you can change the contrast around to adapt the display
  // for the best viewing!
  display.setContrast(50);
  display.clearDisplay();
  
  display.setTextSize(2);
  display.setTextColor(BLACK);
  display.println("The Bedroom"); 
  display.println("Laboratory");

  //delay(5000);
  display.clearDisplay();   // clears the screen and buffer 

  
}
 
void loop()                     // run over and over again
{
 //getting the voltage reading from the temperature sensor
 int reading = analogRead(sensorPin);  
 ledPin = Serial.read(); // this takes in the variable from the control scripts and overrides the led state.
// int reading1 = analogRead (sensorPin1);
 // converting that reading to voltage, for 3.3v arduino use 3.3
 float voltage = reading * 3.3;
 voltage /= 1024.0; 
 
int reading2 = analogRead(sensorPin1);
//Serial.print(reading2); Serial.println("Lux"); // print out the voltage
// Serial.print(voltage); Serial.println(" volts");
 
 // now print out the temperature
 float temperatureC = ((voltage - 0.5) * 100)+24 ;  //converting from 10 mv per degree wit 500 mV offset
                                               //to degrees ((volatge - 500mV) times 100)
 //Serial.print(temperatureC); Serial.println(" degrees C");
 temperatureCOUT= (temperatureC *100);
 // now convert to Fahrenheight
 float temperatureF = (temperatureC * 9.0 / 5.0) + 32.0;
 //Serial.print(temperatureF); Serial.println(" degrees F");
 
  // text display tests
  display.setTextSize(1);
  display.setTextColor(BLACK);
  display.setCursor(0,0);
  display.println("Temperature:");
  display.setTextSize(2);
  display.setTextColor(BLACK);
  display.print(temperatureC); display.println("C");
  display.setTextSize(1);
  display.setTextColor(BLACK);
  display.println("Light");
  display.setTextSize(2);
  display.setTextColor(BLACK);
  display.print(reading2); display.print("Lux");
  // display.print("0x"); display.println(0xDEADBEEF, HEX);
  display.display();

  delay(1000);
  display.clearDisplay();
 
 delay(200);    //waiting 1 seconds


 
 // read the state of the pushbutton value:
  buttonState = digitalRead(buttonPin);

 
 digitalWrite(9,ledPin); // for the serial in
 Serial.print(buttonState);
 Serial.print("?");
 Serial.print(reading2);
 Serial.print("?");
 Serial.print(temperatureCOUT);
 Serial.print("?");
 Serial.println(ledPin);
// Serial.print("?");
// Serial.println(buttonState);
}
