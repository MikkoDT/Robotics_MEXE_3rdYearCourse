import roboticstoolbox as rtb
import math
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3

## Create Model
# link lengths in mm
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))

# link conversion to meter
def mm_to_meter(a):
    m = 1000 # 1 meter = 1000 mm
    return a/m

a1 = mm_to_meter(a1)
a2 = mm_to_meter(a2) 
a3 = mm_to_meter(a3) 
a4 = mm_to_meter(a4) 
 
# link limits converted to meter (d1)
lm1 = float(input("lm1 = "))
lm1 = mm_to_meter(lm1)

# Create links
# [robot_variable]=DHRobot([RevoluteDH(d,r,alpha,offset)])
SCARAV3 = DHRobot([
    PrismaticDH(0,0,(0.0/180.0)*np.pi,a1,qlim=[0,lm1]),
    RevoluteDH(0,a2,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
    RevoluteDH(a3,0,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
    PrismaticDH(0,a4,0,0,qlim=[0,0])
], name="SCARAV3")

print(SCARAV3)

SCARAV3.teach(jointlabels=1)
