
/*
  DigitalReadSerial
 Reads a digital input on pin 2, prints the result to the serial monitor 
 
 This example code is in the public domain.
 */

// digital pin 2 has a pushbutton attached to it. Give it a name:
//int pushButton = 2;
boolean input = false;
boolean transmissionComplete = false;
int sysStatus=0;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  // make the pushbutton's pin an input:
//  pinMode(pushButton, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
    if (transmissionComplete) {
    if(input)
      sysStatus=HIGH;
    else
       sysStatus=LOW; 
    // clear the string:
    transmissionComplete = false;
  } 
  // read the input pin:
//  int buttonState = digitalRead(pushButton);
  // print out the state of the button:
  Serial.print("2?");
  Serial.println(sysStatus);
  delay(2000);        // delay in between reads for stability
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




