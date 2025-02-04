import numpy as np

# links in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))

# joint variables
T1 = float(input("T1 = "))
T2 = float(input("T2 = "))
T3 = float(input("T3 = "))

# degrees to radian
T1 = (T1/180)*np.pi
T2 = (T2/180)*np.pi
T3 = (T3/180)*np.pi

# Parametric Table (theta, alpha, r, d)
PT = [[(0/180)*np.pi+T1,(90/180)*np.pi,0,a1],
      [(90/180)*np.pi+T2,(0/180)*np.pi,a2,0],
      [(0/180)*np.pi+T3,(0/180)*np.pi,a3,0]]

# HTM formula
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

H0_1 = np.array(H0_1)
print("H0_1 = ")
print(H0_1)

H1_2 = np.array(H1_2)
print("H1_2 = ")
print(H1_2)

H2_3 = np.array(H2_3)
print("H2_3 = ")
print(H2_3)

H0_2 = np.dot(H0_1,H1_2)
H0_3 = np.dot(H0_2,H2_3)
print("H0_3 = ")
print(np.array(np.around(H0_3,3)))