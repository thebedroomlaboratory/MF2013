#define DETECT1SENSE 2
#define IR_LED 3
#define DETECT2SENSE 4
#define DETECTPOWER 5
#define RESET 6
#define RELAY 7
#define RESETSUCCESS 13

int count = 0;
boolean FLAG1 = false;
boolean LASTFLAG1 = false;
boolean thisPulse1 = false;

boolean FLAG2 = false;
boolean LASTFLAG2 = false;
boolean thisPulse2 = false;
boolean input = false;         // a string to hold incoming data
boolean transmissionComplete = false;  // whether the string is complete
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
          count=0;
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
  digitalWrite (DETECTPOWER, HIGH);
//  digitalWrite (DETECT2POWER, HIGH);
  TCCR2A |= _BV(COM2B1);
  delayMicroseconds(500);
}

void disablePWM(){
//  Serial.println("Disabling PWM");
  TCCR2A &= ~(_BV(COM2B1));
//  delayMicroseconds(0);
  digitalWrite (IR_LED, LOW);
  digitalWrite (DETECTPOWER, LOW);
//  digitalWrite (DETECT2POWER, LOW);
}

void setup()
{
  Serial.begin(9600);
  setPinsLow();
  
  ADCSRA &= ~(1<<ADEN); //Disable ADC
  ACSR = (1<<ACD); //Disable the analog comparator
  DIDR0 = 0x3F; //Disable digital input buffers on all ADC0-ADC5 pins
  DIDR1 = (1<<AIN1D)|(1<<AIN0D); //Disable digital input buffer on AIN1/0
  enableIROut(38);
////  irsend.enableIROut(38);
}

void loop() {
//  Serial.print("On at: ");
//  Serial.print(millis());
  // Display current pass count on screen and check to see if reset required
//  if(screenCheck()){
  if (transmissionComplete) {
    if(input)
      digitalWrite(RELAY,HIGH);
    else
      digitalWrite(RELAY,LOW); 
    // clear the string:
    transmissionComplete = false;
  }
  resetCheck();
//    irsend.mark(0);
  enablePWM();
  thisPulse1=digitalRead(DETECT1SENSE);
  thisPulse2=digitalRead(DETECT2SENSE);
//  delay(1000);
  disablePWM();

  LASTFLAG1=FLAG1;
  if (thisPulse1){
  // Beam Blocked
    FLAG1=true;
  }
  else {
//  Beam Received
    FLAG1=false;
  }
  
  LASTFLAG2=FLAG2;
  if (thisPulse2){
  // Beam Blocked
    FLAG2=true;
  }
  else {
//  Beam Received
    FLAG2=false;
  }
  
  if(FLAG1 && FLAG2){
    if(!LASTFLAG1 && LASTFLAG2){
      if(count>0)
        count--;
      Serial.print(count);
      Serial.print("?");
      Serial.println(input);
    }
    else if(LASTFLAG1 && !LASTFLAG2){
      count++;
      Serial.print(count);
      Serial.print("?");
      Serial.println(input);
    }
  }

  //display.display();

//  Serial.println(digitalRead(PIN_DETECT));
  

  delay(100);
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar != '\n') {
      if (inChar == '0')
        input=false;
      else if (inChar == '1')
        input=true;
    }
    else {
      transmissionComplete = true;
    }
  }
}
