#include <Servo.h>

int servoPin = 7;
float servoPos = 0;  // Start at home (0 degrees)
float targetPos = 0; // Desired position
Servo myServo;
int t = 10; // Delay between steps (adjust this for speed)

void setup() {
  Serial.begin(9600);
  myServo.attach(servoPin);
  myServo.write(0); // Set home position to 0 degrees
  delay(500); // Give time for the servo to move to home
}

void loop() {
  Serial.println("What Angle for the Servo? ");
  
  while (Serial.available() == 0) {
    // Wait for user input
  }

  targetPos = Serial.parseFloat(); // Get the target angle
  Serial.print("Moving to Angle = ");
  Serial.println(targetPos);
  
  // Move the servo slowly to the target position
  if (targetPos > servoPos) {
    for (float pos = servoPos; pos <= targetPos; pos += 1) { // Increment in small steps
      myServo.write(pos);
      delay(t); // Small delay to slow down movement
    }
  } else {
    for (float pos = servoPos; pos >= targetPos; pos -= 1) { // Decrement in small steps
      myServo.write(pos);
      delay(t);
    }
  }
  
  servoPos = targetPos; // Update current position
}
