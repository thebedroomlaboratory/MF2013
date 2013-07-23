#include "LowPower.h"

#define IR_LED 3
#define DETECT1SENSE 4
#define DETECT1POWER 5
#define RESET 6
#define RELAY 7
#define DETECT2SENSE 8
#define DETECT2POWER 9
#define RESETSUCCESS 13

int x = 0;
boolean lastPulseSuccess1 = true;
boolean thisPulse1 = false;
boolean lastPulseSuccess2 = true;
boolean thisPulse2 = false;
//boolean screenChecked = false;

void setPinsLow(){
  for (byte i = 0; i <= 13; i++)
  {
    pinMode (i, OUTPUT);    // changed as per below
    digitalWrite (i, LOW);  //     ditto
  }
  pinMode(DETECT1SENSE, INPUT);
  pinMode(DETECT2SENSE, INPUT);
  pinMode(RESET, INPUT);
}


void resetCheck(){
  // Check if reset switch is on
  if(digitalRead(RESET)==HIGH){
    delay(1000); 
    if(digitalRead(RESET)==HIGH){
      delay(1000); 
      if(digitalRead(RESET)==HIGH){
        delay(1000); 
        if(digitalRead(RESET)==HIGH){
          x=0;
          // Flash internal LED to show that value has been reset
          digitalWrite(RESETSUCCESS, HIGH);
          delay(1000);
          digitalWrite(RESETSUCCESS, LOW);
        }
      }
    }
  }
}

void enableIROut(int val){
  TIMSK2 = 0;
  const uint8_t pwmval = F_CPU / 2000 / (val); \
  TCCR2A = _BV(WGM20); \
  TCCR2B = _BV(WGM22) | _BV(CS20); \
  OCR2A = pwmval; \
  OCR2B = pwmval / 3; 
//  Serial.println("PWM Setup"); 
}

void enablePWM(){
//  Serial.println("Enabling PWM");
  digitalWrite (DETECT1POWER, HIGH);
  digitalWrite (DETECT2POWER, HIGH);
  TCCR2A |= _BV(COM2B1);
  delayMicroseconds(500);
}

void disablePWM(){
//  Serial.println("Disabling PWM");
  TCCR2A &= ~(_BV(COM2B1));
//  delayMicroseconds(0);
  digitalWrite (IR_LED, LOW);
  digitalWrite (DETECT1POWER, LOW);
  digitalWrite (DETECT2POWER, LOW);
}

void setup()
{
//  Serial.begin(9600);
  setPinsLow();
  
  ADCSRA &= ~(1<<ADEN); //Disable ADC
  ACSR = (1<<ACD); //Disable the analog comparator
  DIDR0 = 0x3F; //Disable digital input buffers on all ADC0-ADC5 pins
  DIDR1 = (1<<AIN1D)|(1<<AIN0D); //Disable digital input buffer on AIN1/0
  enableIROut(38);
//  irsend.enableIROut(38);
}

void loop() {
//  Serial.print("On at: ");
//  Serial.print(millis());
  // Display current pass count on screen and check to see if reset required
//  if(screenCheck()){
  resetCheck();
//    irsend.mark(0);
  enablePWM();
  thisPulse1=digitalRead(DETECT1SENSE);
  thisPulse2=digitalRead(DETECT2SENSE);
//    delay(1000);
  disablePWM();
//    irsend.space(0);
//    Serial.print("Off at: ");
//    Serial.println(millis());
  if (thisPulse1){
    if(lastPulseSuccess1){
      x++;
      lastPulseSuccess1=false;
//      display.print("Break: ");
//      display.println(x);
//        Serial.println(" times");
    }
//    else {
//      display.println("Still broken");
//    }
  }
  else {
//    display.println("Received");
    lastPulseSuccess1=true;
  }
  //display.display();

//  Serial.println(digitalRead(PIN_DETECT));
//  Serial.print("Off at: ");
//  Serial.println(x);
//  Serial.flush();
  LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);
}
