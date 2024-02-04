import numpy as np

#Inverse Kinematics Using Graphical Method

#link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))

#Position Vector in mm
xe = float(input("X = "))
ye = float(input("Y = "))
ze = float(input("Z = "))

# To solve for Theta 2 or Th2
phi2 = np.arctan(ye/xe) #1
r1 = np.sqrt(ye**2 + xe**2) #2
phi1 = np.arccos((a4**2 - a2**2 - r1**2)/(-2 * a2 * r1)) #3
Th2 = (phi2 - phi1) * 180/np.pi #4

# To solve for Theta 3 or Th3
phi3 = np.arccos((r1**2 - a2**2 - a4**2)/(-2 * a2 * a4)) #5
Th3 = 180 - (phi3*180/np.pi) #6

# To solve for D1
D1 = ze - a1 - a3 #7

print("D1 = ", np.around(D1,3))

print("Th2 = ", np.around(Th2,3))

print("Th3 = ", np.around(Th3,3))