#include <Servo.h>

// Define servo objects
Servo servo1, servo2, servo3, servo4;

// Define servo pins
int servoPins[] = {3, 4, 5, 7}; // Servo 1 to Servo 4

// Servo positions (starting at 0 degrees)
float servoPos[] = {0, 0, 0, 0};
float targetPos[] = {0, 0, 0, 0}; // Desired positions for all servos
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
  Serial.println("Enter 4 angles separated by spaces (e.g., 30 60 90 120): ");

  while (Serial.available() == 0) {
    // Wait for user input
  }

  // Read and parse four angles
  for (int i = 0; i < 4; i++) {
    targetPos[i] = Serial.parseFloat(); // Read each angle
    if (targetPos[i] < 0 || targetPos[i] > 180) {
      Serial.println("Invalid angle! Please enter values between 0 and 180.");
      return;
    }
  }

  Serial.println("Moving servos to target positions...");

  // Move all servos gradually
  moveAllServosGradually();
}

void moveAllServosGradually() {
  bool moving = true;

  while (moving) {
    moving = false;

    // Move each servo step by step
    for (int i = 0; i < 4; i++) {
      if (servoPos[i] < targetPos[i]) {
        servoPos[i] += 1;
        moving = true;
      } else if (servoPos[i] > targetPos[i]) {
        servoPos[i] -= 1;
        moving = true;
      }

      // Apply new position
      switch (i) {
        case 0: servo1.write(servoPos[i]); break;
        case 1: servo2.write(servoPos[i]); break;
        case 2: servo3.write(servoPos[i]); break;
        case 3: servo4.write(servoPos[i]); break;
      }
    }

    delay(t); // Delay to slow down the movement
  }
}
