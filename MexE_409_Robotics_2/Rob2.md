# Robotics 2

# 1. D-H Notation

<img width="350" alt="D-H N" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/031a0762-396d-4da9-ac0f-0684a220d31f">

### Step 1: Assign Frames according to the 4 D-H Frame Rules
![image](https://github.com/user-attachments/assets/5b826305-30ec-4325-8116-14664a11f50c)

### Step 2: Fill out the D-H Parametric Table
![image](https://github.com/user-attachments/assets/4b259be4-a14e-46d4-b24d-ad7c818d384d)

### Step 3: Plug the table into the Homogeneous Transformation Matrix formula.
![image](https://github.com/user-attachments/assets/7b7cebca-0c8e-42a3-90a5-0bef1424b3d6)
![image](https://github.com/user-attachments/assets/9ee3b9d7-9c72-46b9-bb1d-39bf117e5dd2)
![image](https://github.com/user-attachments/assets/2a198bc1-6872-4169-beff-08a71dff1b80)
![image](https://github.com/user-attachments/assets/dbdf4db5-e810-4b9a-84c6-31ecfdee40f5)

Example 1:

Step 3: Plug the table into the Homogeneous Transformation Matrix formula.

<img width="400" alt="Example" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/dd9f01ae-e27d-45e3-8688-25b7509832ef">

Step 4: Multiply the matrices together

<img width="226" alt="HTM" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/5dd047c7-7b3b-47d4-bb9e-2f7dd596f7b8">

# 2. Forward Kinemtics

<img width="475" alt="FK1" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/e42568c6-3e60-4fb1-b26a-5918474e1986">

Example:

<img width="500" alt="FK2" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/74ee324e-88f3-4d76-b214-d42160d72b8b">

Any of the 2 processes, it will still arrive on the same answer.

<img width="500" alt="FK3" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/b7b068a2-2570-48a6-aea4-f1f53227d67a">

Determining the position and direction using Forward Kinematics.

<img width="500" alt="FK4" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/495ddfd2-0eed-44fe-82b6-77b8e831553e">

Simulation and visualization of Forward Kinematics using MATLAB:

If θ1=0֯ and θ2=0֯:

<img width="400" alt="Pract3 1" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/d6841e9e-02e9-4e74-a2b3-5c151db5ec96">

If θ1=90֯ and θ2=-90֯:

<img width="400" alt="Pract3 2" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/2668d6ae-5a32-4468-be03-90672eaf78ff">

If θ1=45֯ and θ2=30֯:

<img width="400" alt="Pract3 3" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/404a2146-a4bc-4aa2-8e60-b0525b733c7a">

# 2.1 Forward Kinematics in Python and MATLAB

Codes can also be found from: https://github.com/MikkoDT/Robotics-2-2022-2023
And the tutorial for installation of Robotics Toolbox by Peter Corke in Python can be found here: https://youtube.com/playlist?list=PLUgsbeZHs9qMFXTIQPW0clLoRkf_oiBoX&si=0sYu2QIJ4NWilTq7


# spartankit_test.py of 3-DOF SPARTAN Robotkit 
[Project code](https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/blob/main/MexE_409_Robotics_2/Python_programs/Programs_2024_2025/spartankit_test.py)

# MATLAB of 3-DOF SPARTAN Robotkit
[Project code](https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/tree/main/MexE_409_Robotics_2/MATLAB_sample_programs/2024-2025)

# 4. Spherical Wrists

<img width="350" alt="spherical_wrists" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/cbf6bf4e-3f9f-42f0-acbe-7b67684249a9">

SCARA PRR Variant 3

3-DOF

<img width="350" alt="3-dof" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/4ba08d84-5d00-416c-b482-3d0347606ce5">

6-DOF

<img width="350" alt="6-DOF" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/e7d7846c-06cc-4ce2-b45a-3e24271c0471">

# 5. Inverse Kinematics

<img width="500" alt="Ik" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/7a563629-3245-4294-8285-bd52bbf7c681">

 # Graphical Method for Solving Inverse Kinematics

 <img width="500" alt="GM" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/b8ec56c4-ddf1-429a-9a4d-ee6b8d07755b">

* Example:

<img width="400" alt="example1" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/fa95b903-8e36-4d35-a68f-e73ef852fc57">

<img width="400" alt="IK2D" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/68eab695-6b4a-460b-83c1-ce46cd5e8bc0">

# 5.1 Inverse Kinematics of Cartesian Manipulator

<img width="439" alt="CartIK" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/b20a8db9-9d4b-4375-b867-37392ea1f331">

<img width="400" alt="CartIK2" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/310f8600-8fab-4073-8580-aafc1ca042d1">

<img width="400" alt="CartIK3" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/d47c556a-6965-424d-8c09-3905327f1c7b">

5.2 Inverse Kinematics of Articulated Manipulator

<img width="500" alt="IKArt" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/1d8daa29-7eab-438b-b8ac-2029a7b2cd3f">

<img width="500" alt="Arttop" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/6dc2130a-cc45-4a81-b808-fd81d694c2d7">

<img width="500" alt="FrArt" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/5c8250fb-2c90-4cfc-a012-029be5333120">

# 5.3 Inverse Kinematics in Python

Codes can also be found from: https://github.com/MikkoDT/Robotics-2-2022-2023

<img width="500" alt="SCV3" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/36bc8b9f-4c40-44be-bd38-4bc0fd7bc5d9">

<img width="400" alt="IK3" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/487495ff-0083-46f7-80d5-7e185f6f7a1e">

<img width="418" alt="IK3-1" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/b2060b2d-6a37-4918-a5e2-7c616104ce90">

# IKin.py of SCARA-V3

### Inverse Kinematics of SCARA-V3
import numpy as np

# link lengths in mm
a1 = float(input("a1 = "))

a2 = float(input("a2 = "))

a3 = float(input("a3 = "))

a4 = float(input("a4 = "))

# Position Vector in mm
x0_3 = float(input("x0_3 = "))

y0_3 = float(input("y0_3 = "))

z0_3 = float(input("z0_3 = "))

# Inverse Kinematic Solutions using Graphical Method

# Solution 1
phi2 = np.arctan(y0_3 / x0_3)

phi2 = phi2 * 180 / np.pi

# Solution 2
r1 = np.sqrt((y0_3**2) + (x0_3**2))

# Solution 3
phi1 = np.arccos((a4**2 - r1**2 - a2**2)/(-2 * r1 * a2))

phi1 = phi1*180 / np.pi

# Solution 4
theta2 = phi2 - phi1

# solution 5
phi3 = np.arccos((r1**2 - a2**2 - a4**2)/(-2 * a2 * a4))

phi3 = phi3 * 180 / np.pi

# Solution 6
theta3 = 180 - phi3

# Solution 7
d1 = z0_3 - a1 - a3

# Displaying the Joint Variables
print("d1 = ", np.around(d1,3))

print("theta2 = ", np.around(theta2,3))

print("theta3 = ", np.around(theta3,3))
