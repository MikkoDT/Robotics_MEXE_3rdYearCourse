#include <Servo.h>

// Define servo objects
Servo servo1, servo2, servo3, servo4;

// Define servo pins
int servoPins[] = {3, 4, 5, 7}; // Servo 1 to Servo 4

// Servo positions (starting at 0 degrees)
float servoPos[] = {0, 0, 0, 0};
float targetPos = 0; // Desired position
int selectedServo = 0; // Servo to control (0-3)
int t = 20; // Delay between steps (adjust for speed)

void setup() {
  Serial.begin(9600);

  // Attach servos to their respective pins
  servo1.attach(servoPins[0]);
  servo2.attach(servoPins[1]);
  servo3.attach(servoPins[2]);
  servo4.attach(servoPins[3]);

  // Set all servos to home position (0 degrees)
  servo1.write(0);
  servo2.write(0);
  servo3.write(0);
  servo4.write(0);
  
  delay(500); // Allow time for servos to reach home position
}

void loop() {
  Serial.println("Select Servo (1-4): ");

  while (Serial.available() == 0) {
    // Wait for user input
  }

  selectedServo = Serial.parseInt() - 1; // Convert user input (1-4) to index (0-3)
  
  if (selectedServo < 0 || selectedServo > 3) {
    Serial.println("Invalid servo number! Please enter 1 to 4.");
    return;
  }

  Serial.print("Servo ");
  Serial.print(selectedServo + 1);
  Serial.println(" selected. Enter angle (0-180): ");

  while (Serial.available() == 0) {
    // Wait for user input
  }

  targetPos = Serial.parseFloat(); // Get the target angle

  if (targetPos < 0 || targetPos > 180) {
    Serial.println("Invalid angle! Please enter 0 to 180.");
    return;
  }

  Serial.print("Moving Servo ");
  Serial.print(selectedServo + 1);
  Serial.print(" to ");
  Serial.print(targetPos);
  Serial.println(" degrees.");

  // Move the selected servo gradually
  moveServoGradually(selectedServo, targetPos);
}

void moveServoGradually(int servoIndex, float target) {
  if (servoIndex < 0 || servoIndex > 3) return;

  Servo* selectedServoObj;

  // Select the correct servo object
  switch (servoIndex) {
    case 0: selectedServoObj = &servo1; break;
    case 1: selectedServoObj = &servo2; break;
    case 2: selectedServoObj = &servo3; break;
    case 3: selectedServoObj = &servo4; break;
  }

  // Move the servo smoothly
  if (target > servoPos[servoIndex]) {
    for (float pos = servoPos[servoIndex]; pos <= target; pos += 1) {
      selectedServoObj->write(pos);
      delay(t);
    }
  } else {
    for (float pos = servoPos[servoIndex]; pos >= target; pos -= 1) {
      selectedServoObj->write(pos);
      delay(t);
    }
  }

  servoPos[servoIndex] = target; // Update current position
}
