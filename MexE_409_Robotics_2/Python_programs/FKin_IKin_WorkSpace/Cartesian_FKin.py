import numpy as np

# link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))

# joint variables: is mm if d, is degrees if theta
d1 = float(input("d1 = "))
d2 = float(input("d2 = ")) 
d3 = float(input("d3 = ")) 

# Parametric Table (theta, alpha, r, d)
PT = [
      [0, (270/180)*np.pi, 0, a1], 
      [(270/180)*np.pi, (270/180)*np.pi, 0, a2+d1], 
      [(90/180)*np.pi, (270/180)*np.pi, 0, a3+d2],
      [0, 0, 0, a4+d3]
      ] 
#3x3 size row x column

# HTM formulae
i = 0 #to not manually change index/positions
H0_1 = [
        [np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]), np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]), np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT[i][0])],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]
        ]

i = 1
H1_2 = [
        [np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]), np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]), np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT[i][0])],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]
        ]

i = 2
H2_3 = [
        [np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]), np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]), np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT[i][0])],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]
        ]

i = 3
H3_4 = [
        [np.cos(PT[i][0]), -np.sin(PT[i][0])*np.cos(PT[i][1]), np.sin(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.cos(PT[i][0])],
        [np.sin(PT[i][0]), np.cos(PT[i][0])*np.cos(PT[i][1]), -np.cos(PT[i][0])*np.sin(PT[i][1]), PT[i][2]*np.sin(PT[i][0])],
        [0, np.sin(PT[i][1]), np.cos(PT[i][1]), PT[i][3]],
        [0, 0, 0, 1]
        ]

H0_1 = np.array(H0_1)
print("H0_1= ")
print(np.around(H0_1,3))

H1_2 = np.array(H1_2)
print("H1_2= ")
print(np.around(H1_2,3))

H2_3 = np.array(H2_3)
print("H2_3= ")
print(np.around(H2_3,3))

H3_4 = np.array(H3_4)
print("H3_4= ")
print(np.around(H3_4,3))

H0_2 = np.dot(H0_1,H1_2)
H0_3 = np.dot(H0_2,H2_3)
H0_4 = np.dot(H0_3,H3_4)
print("H0_4= ")
print(np.around(H0_4,3))
