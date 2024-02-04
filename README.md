# Robotics 2

# 1. Spherical Manipulators

<img width="350" alt="spherical_wrists" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/cbf6bf4e-3f9f-42f0-acbe-7b67684249a9">

SCARA PRR Variant 3

3-DOF

<img width="350" alt="3-dof" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/4ba08d84-5d00-416c-b482-3d0347606ce5">

6-DOF

<img width="350" alt="6-DOF" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/e7d7846c-06cc-4ce2-b45a-3e24271c0471">

# 2. D-H Notation

<img width="350" alt="D-H N" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/031a0762-396d-4da9-ac0f-0684a220d31f">

Example:

Step 3: Plug the table into the Homogeneous Transformation Matrix formula.

<img width="400" alt="Example" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/dd9f01ae-e27d-45e3-8688-25b7509832ef">

Step 4: Multiply the matrices together

<img width="226" alt="HTM" src="https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/assets/93197249/5dd047c7-7b3b-47d4-bb9e-2f7dd596f7b8">

# 3. Forward Kinemtics

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

# 3.1 Forward Kinematics in Python and MATLAB

Codes can also be found from: https://github.com/MikkoDT/Robotics-2-2022-2023
And the tutorial for installation of Robotics Toolbox by Peter Corke in Python can be found here: https://youtube.com/playlist?list=PLUgsbeZHs9qMFXTIQPW0clLoRkf_oiBoX&si=0sYu2QIJ4NWilTq7

**FKin.py of SCARA-V3**

**Import librariies first for scientific and matric computations**
import numpy as np 

import math

**link lengths in mm**
a1 = float(input("a1 = "))

a2 = float(input("a2 = "))

a3 = float(input("a3 = "))

a4 = float(input("a4 = "))

**joint variables: is mm if f, is degrees if theta**
d1 = float(input("d1 = ")) #20 mm

T2 = float(input("T2 = ")) #30 deg

T3 = float(input("T3 = ")) #-90 deg

**degree to radian**
T2 = (T2/180.0)*np.pi

T3 = (T3/180.0)*np.pi

**Parametric Table (theta, alpha, r, d)**
PT = [[(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,0,a1+d1],

      [T2,(0.0/180.0)*np.pi,a2,0],
      
      [T3,(0.0/180.0)*np.pi,a4,a3]]


**HTM formula and multiplication**
i = 0
H0_1 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],

        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        
        [0,0,0,1]]

i = 1
H1_2 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],

        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        
        [0,0,0,1]]

i = 2
H2_3 = [[np.cos(PT[i][0]),-np.sin(PT[i][0])*np.cos(PT[i][1]),np.sin(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.cos(PT[i][0])],

        [np.sin(PT[i][0]),np.cos(PT[i][0])*np.cos(PT[i][1]),-np.cos(PT[i][0])*np.sin(PT[i][1]),PT[i][2]*np.sin(PT[i][0])],
        
        [0,np.sin(PT[i][1]),np.cos(PT[i][1]),PT[i][3]],
        
        [0,0,0,1]]
        
**Multiply the matrices**
H0_1 = np.matrix(H0_1)

print("H0_1= ")

print(H0_1)

H1_2 = np.matrix(H1_2)

print("H1_2= ")

print(H1_2)

H2_3 = np.matrix(H2_3)

print("H2_3= ")

print(H2_3)

H0_2 = np.dot(H0_1,H1_2)

H0_3 = np.dot(H0_2,H2_3)

print("H0_3= ")

print(np.matrix(np.around(H0_3,3)))


