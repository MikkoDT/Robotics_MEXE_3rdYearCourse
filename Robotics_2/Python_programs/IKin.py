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
phi2 = np.arctan(y0_3/x0_3)
phi2 = phi2*180/np.pi

# Solution 2
r1 = np.sqrt((y0_3**2)+(x0_3**2))

# Solution 3
phi1 = np.arccos((a4**2-r1**2-a2**2)/(-2*r1*a2))
phi1 = phi1*180/np.pi

# Solution 4
theta2 = phi2 - phi1

# solution 5
phi3 = np.arccos((r1**2-a2**2-a4**2)/(-2*a2*a4))
phi3 = phi3*180/np.pi

# Solution 6
theta3 = 180 - phi3

# Solution 7
d1 = z0_3 - a1 - a3

print("d1 = ", np.around(d1,3))
print("theta2 = ", np.around(theta2,3))
print("theta3 = ", np.around(theta3,3))