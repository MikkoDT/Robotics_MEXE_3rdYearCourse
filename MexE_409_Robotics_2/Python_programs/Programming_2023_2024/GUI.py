# The code below is importing the necessary libraries for the program to run.
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import numpy as np
import math
import roboticstoolbox as rtb
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH
import spatialmath
from spatialmath import SE3
import matplotlib
matplotlib.use('TkAgg')

# Creating a GUI window with a title and an icon.
gui = Tk()
gui.title("SCARA_V3 Design Calculator")
gui.resizable(False,False)
gui.config(bg="green")

def reset():
    """
    It clears all the text boxes.
    """
    a1_E.delete(0, END)
    a2_E.delete(0, END)
    a3_E.delete(0, END)
    a4_E.delete(0, END)

    d1_E.delete(0, END)
    t2_E.delete(0, END)
    t3_E.delete(0, END)
    
    X_E.delete(0, END)
    Y_E.delete(0, END)
    Z_E.delete(0, END)

def f_k():
 
    """
    It calculates the forward kinematics of the robot.
    """
    a1 = float(a1_E.get())
    a2 = float(a2_E.get())
    a3 = float(a3_E.get())
    a4 = float(a4_E.get())

    d1 = float(d1_E.get())
    T2 = float(t2_E.get())
    T3 = float(t3_E.get())


    T2 = (T2/180.0)*np.pi # Theta 2 in radians
    T3 = (T3/180.0)*np.pi # Theta 3 in radians

    PT = [[(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,0,a1+d1],
          [T2,(0.0/180.0)*np.pi,a2,0],
          [T3,(0.0/180.0)*np.pi,a4,a3]]

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

    # Position/Translation Joints
    H0_1 = np.matrix(H0_1) 

    H1_2 = np.matrix(H1_2) 

    H2_3 = np.matrix(H2_3) 

    H0_2 = np.dot(H0_1,H1_2)
    H0_3 = np.dot(H0_2,H2_3)

    X0_3 = H0_3[0,3]
    X_E.delete(0,END)
    X_E.insert(0,np.around(X0_3,3))
    Y0_3 =H0_3[1,3]
    Y_E.delete(0,END)
    Y_E.insert(0,np.around(Y0_3,3))
    Z0_3 =H0_3[2,3]
    Z_E.delete(0,END)
    Z_E.insert(0,np.around(Z0_3,3))

## Jacobian Matrix

    # Jacobian Window
    J_sw = Toplevel()
    J_sw.title("Velocity Calculator")
    J_sw.resizable(False,False)

    #1. Linear / Prismatic Vectors
    Z_1 = [[0],[0],[1]] # The [0,0,1] vector

     #Row 1 to 3, Column 1
    J1 = [[1,0,0],[0,1,0],[0,0,1]]
    J1 = np.dot(J1,Z_1)
    J1 = np.matrix(J1)

     #Row 1 to 3, Column 2
    J2a = H0_1[0:3,0:3]
    J2a = np.dot(J2a,Z_1)

    J2b_1 = H0_3[0:3,3:]
    J2b_1 = np.matrix(J2b_1)

    J2b_2 = H0_1[0:3,3:]
    J2b_2 = np.matrix(J2b_2)

    J2b = J2b_1 - J2b_2

    J2 = [[(J2a[1,0]*J2b[2,0])-(J2a[2,0]*J2b[1,0])],
            [(J2a[2,0]*J2b[0,0])-(J2a[0,0]*J2b[2,0])],
            [(J2a[0,0]*J2b[1,0])-(J2a[1,0]*J2b[0,0])]]
    
    J2 = np.matrix(J2)

     #Row 1 to 3, Column 3
    J3a = H0_2[0:3,0:3]
    J3a = np.dot(J3a,Z_1)

    J3b_1 = H0_3[0:3,3:]
    J3b_1 = np.matrix(J3b_1)

    J3b_2 = H0_2[0:3,3:]
    J3b_2 = np.matrix(J3b_2)

    J3b = J3b_1 - J3b_2

    J3 = [[(J3a[1,0]*J3b[2,0])-(J3a[2,0]*J3b[1,0])],
        [(J3a[2,0]*J3b[0,0])-(J3a[0,0]*J3b[2,0])],
        [(J3a[0,0]*J3b[1,0])-(J3a[1,0]*J3b[0,0])]]

    J3 = np.matrix(J3)

    #2. Rotation / Orientation Vectors

        #Row 4 to 6, Column 1
    J4 = [[0],[0],[0]]
    J4 = np.matrix(J4)

        #Row 4 to 6, Column 2
    J5 = J2a
    J5 = np.matrix(J5)
        #Row 4 to 6, Column 3
    J6 = J3a
    J6 = np.matrix(J6)

    #3. Concatenated Jacobian Matrix
    JM1 = np.concatenate((J1,J2,J3),1)
    JM2 = np.concatenate((J4,J5,J6),1)

    J = np.concatenate((JM1,JM2),0)
    J = np.matrix(J)

    def update_velo():
        d1p = d1_slider.get()
        T2p = T2_slider.get()
        T3p = T3_slider.get()

        q = np.array([[d1p],[T2p],[T3p]])
        E = np.dot(J,q)

        xp_e = E[0,0]
        x_entry.delete(0,END)
        x_entry.insert(0,str(xp_e))

        yp_e = E[1,0]
        y_entry.delete(0,END)
        y_entry.insert(0,str(yp_e))

        zp_e = E[2,0]
        z_entry.delete(0,END)
        z_entry.insert(0,str(zp_e))

        ωx_e = E[3,0]
        ωx_entry.delete(0,END)
        ωx_entry.insert(0,str(ωx_e))

        ωy_e = E[4,0]
        ωy_entry.delete(0,END)
        ωy_entry.insert(0,str(ωy_e))

        ωz_e = E[5,0]
        ωz_entry.delete(0,END)
        ωz_entry.insert(0,str(ωz_e))

# Jacobian Sliders

    d1_velo = Label(J_sw,text=("d1* = "),font=(5)) 
    d1_slider = Scale(J_sw,from_=0,to_=30,orient=HORIZONTAL,length=100)
    d1_unit = Label(J_sw,text=("cm/s"),font=(5))

    T2_velo = Label(J_sw,text=("θ2* = "),font=(5)) 
    T2_slider = Scale(J_sw,from_=0,to_=3.142,orient=HORIZONTAL,length=100,sliderlength=10)
    T2_unit = Label(J_sw,text=("rad/s"),font=(5))

    T3_velo = Label(J_sw,text=("θ3* = "),font=(5)) 
    T3_slider = Scale(J_sw,from_=0,to_=3.142,orient=HORIZONTAL,length=100,sliderlength=10)
    T3_unit = Label(J_sw,text=("rad/s"),font=(5))

    d1_velo.grid(row=0,column=0)
    d1_slider.grid(row=0,column=1)
    d1_unit.grid(row=0,column=2)

    T2_velo.grid(row=1,column=0)
    T2_slider.grid(row=1,column=1)
    T2_unit.grid(row=1,column=2)

    T3_velo.grid(row=2,column=0)
    T3_slider.grid(row=2,column=1)
    T3_unit.grid(row=2,column=2)

# Jacobian Entries and Labels
    x_velo = Label(J_sw,text=("x* = "),font=(5)) 
    x_entry = Entry(J_sw,width=10,font=(10))
    x_unit = Label(J_sw,text=("cm/s"),font=(5))
    x_velo.grid(row=3,column=0)
    x_entry.grid(row=3,column=1)
    x_unit.grid(row=3,column=2)

    y_velo = Label(J_sw,text=("y* = "),font=(5)) 
    y_entry = Entry(J_sw,width=10,font=(10))
    y_unit = Label(J_sw,text=("cm/s"),font=(5))
    y_velo.grid(row=4,column=0)
    y_entry.grid(row=4,column=1)
    y_unit.grid(row=4,column=2)

    z_velo = Label(J_sw,text=("z* = "),font=(5)) 
    z_entry = Entry(J_sw,width=10,font=(10))
    z_unit = Label(J_sw,text=("cm/s"),font=(5))
    z_velo.grid(row=5,column=0)
    z_entry.grid(row=5,column=1)
    z_unit.grid(row=5,column=2)

    ωx_velo = Label(J_sw,text=("ωx = "),font=(5)) 
    ωx_entry = Entry(J_sw,width=10,font=(10))
    ωx_unit = Label(J_sw,text=("rad/s"),font=(5))
    ωx_velo.grid(row=6,column=0)
    ωx_entry.grid(row=6,column=1)
    ωx_unit.grid(row=6,column=2)

    ωy_velo = Label(J_sw,text=("ωy = "),font=(5)) 
    ωy_entry = Entry(J_sw,width=10,font=(10))
    ωy_unit = Label(J_sw,text=("rad/s"),font=(5))
    ωy_velo.grid(row=7,column=0)
    ωy_entry.grid(row=7,column=1)
    ωy_unit.grid(row=7,column=2)

    ωz_velo = Label(J_sw,text=("ωz = "),font=(5)) 
    ωz_entry = Entry(J_sw,width=10,font=(10))
    ωz_unit = Label(J_sw,text=("rad/s"),font=(5))
    ωz_velo.grid(row=8,column=0)
    ωz_entry.grid(row=8,column=1)
    ωz_unit.grid(row=8,column=2)

    # Update Button
    update_but = Button(J_sw,text="Update",bg="green",fg="white",command=update_velo)
    update_but.grid(row=9,column=0)

    # Create Links
    SCARA_V3 = DHRobot([
            PrismaticDH(0,0,(0/180)*np.pi,a1/100,qlim=[0,(30/100)]),
            RevoluteDH(0,a2/100,(0/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
            RevoluteDH(a3/100,0,(0/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
            PrismaticDH(0,a4/100,0,0,qlim=[0,0])

        ], name='SCARA_V3')

    #plot joints
    q1 = np.array([d1/100,T2,T3,0])

    #plot scale
    x1 = -0.5
    x2 = 0.5
    y1 = -0.5
    y2 = 0.5
    z1 = 0.0
    z2 = 0.5     

    # Plot commands
    SCARA_V3.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)

def i_k():
    #Inverse Kinematics Using Graphical Method

    #link lengths in cm
    a1 = float(a1_E.get())
    a2 = float(a2_E.get())
    a3 = float(a3_E.get())
    a4 = float(a4_E.get())

    #Position Vector in cm
    xe = float(X_E.get())
    ye = float(Y_E.get())
    ze = float(Z_E.get())

    # To solve for Theta 2 or Th2
    phi2 = np.arctan(ye/xe) #1
    r1 = np.sqrt(ye**2 + xe**2) #2
    phi1 = np.arccos((a4**2 - a2**2 - r1**2)/(-2 * a2 * r1)) #3
    Th2 = phi2 - phi1 #4

    # To solve for Theta 3 or Th3
    phi3 = np.arccos((r1**2 - a2**2 - a4**2)/(-2 * a2 * a4)) #5
    Th3 = np.pi - phi3 #6

    # To solve for D1
    D1 = ze - a1 - a3 #7

    d1_E.delete(0,END)
    d1_E.insert(0,np.around(D1,3))

    t2_E.delete(0,END)
    t2_E.insert(0,np.around(Th2*180/np.pi,3))

    t3_E.delete(0,END)
    t3_E.insert(0,np.around(Th3*180/np.pi,3))

    # Create Links
    SCARA_V3 = DHRobot([
            PrismaticDH(0,0,(0/180)*np.pi,a1/100,qlim=[0,(30/100)]),
            RevoluteDH(0,a2/100,(0/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
            RevoluteDH(a3/100,0,(0/180)*np.pi,0,qlim=[(-90/180)*np.pi,(90/180)*np.pi]),
            PrismaticDH(0,a4/100,0,0,qlim=[0,0])

        ], name='SCARA_V3')

    #plot joints
    q1 = np.array([D1/100,Th2,Th3,0])

    #plot scale
    x1 = -0.5
    x2 = 0.5
    y1 = -0.5
    y2 = 0.5
    z1 = 0.0
    z2 = 0.5     

    # Plot commands
    SCARA_V3.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)

# Link Lengths and Joint Variables Frame
FI = LabelFrame(gui,text="Link Lengths and Joint Variables",font=(5))
FI.grid(row=0,column=0)

# The code below is creating a label frame and 
# then creating labels and entries for the link lengths.
#Link lengths
a1 = Label(FI,text=("a1 = "),font=(10))
a1_E = Entry(FI,width=5,font=(10))
cm1 = Label(FI,text=("cm"),font=(10))

a2 = Label(FI,text=("a2 = "),font=(10))
a2_E = Entry(FI,width=5,font=(10))
cm2 = Label(FI,text=("cm"),font=(10))

a3 = Label(FI,text=("a3 = "),font=(10))
a3_E = Entry(FI,width=5,font=(10))
cm3 = Label(FI,text=("cm"),font=(10))

a4 = Label(FI,text=("a4 = "),font=(10))
a4_E = Entry(FI,width=5,font=(10))
cm4 = Label(FI,text=("cm"),font=(10))

a1.grid(row=0,column=0)
a1_E.grid(row=0,column=1)
cm1.grid(row=0,column=2)

a2.grid(row=1,column=0)
a2_E.grid(row=1,column=1)
cm2.grid(row=1,column=2)

a3.grid(row=2,column=0)
a3_E.grid(row=2,column=1)
cm3.grid(row=2,column=2)

a4.grid(row=3,column=0)
a4_E.grid(row=3,column=1)
cm4.grid(row=3,column=2)

# The code below is creating a label frame and 
# then creating labels and entries for the Joint Variables.
# Joint Variables
d1 = Label(FI,text=("d1 = "),font=(10))
d1_E = Entry(FI,width=5,font=(10))
cm7 = Label(FI,text=("cm"),font=(10))

t2 = Label(FI,text=("t2 = "),font=(10))
t2_E = Entry(FI,width=5,font=(10))
deg2 = Label(FI,text=("deg"),font=(10))

t3 = Label(FI,text=("t3 = "),font=(10))
t3_E = Entry(FI,width=5,font=(10))
deg3 = Label(FI,text=("deg"),font=(10))

d1.grid(row=0,column=3)
d1_E.grid(row=0,column=4)
cm7.grid(row=0,column=5)

t2.grid(row=1,column=3)
t2_E.grid(row=1,column=4)
deg2.grid(row=1,column=5)

t3.grid(row=2,column=3)
t3_E.grid(row=2,column=4)
deg3.grid(row=2,column=5)

# The code below is creating a frame and buttons.
# Buttons Frame
BF = LabelFrame(gui,text="Forward & Inverse Kinematics",font=(5))
BF.grid(row=1,column=0)

# Buttons
FK = Button(BF,text="↓ Forward",font=(10),bg="blue",fg="white",command=f_k)
rst = Button(BF,text="RESET",font=(10),bg="green",fg="white",command=reset)
IK = Button(BF,text="↑ Inverse",font=(10),bg="red",fg="white",command=i_k)

FK.grid(row=0,column=0)
rst.grid(row=0,column=1)
IK.grid(row=0,column=2)

# The code below is creating a label frame, which is a frame that contains labels. The label frame is
# called PV, and it is placed in the gui window. The label frame is given the title "Position
# Vectors", and the font is set to 5. The label frame is placed in the second row and the first
# column.

# Position Vectors Frame
PV = LabelFrame(gui,text="Position Vectors",font=(5))
PV.grid(row=2,column=0)

# Position Vector
X = Label(PV,text=("X = "),font=(10))
X_E = Entry(PV,width=8,font=(10))
cm8 = Label(PV,text=("cm"),font=(10))

Y = Label(PV,text=("Y = "),font=(10))
Y_E = Entry(PV,width=8,font=(10))
cm9 = Label(PV,text=("cm"),font=(10))

Z = Label(PV,text=("Z = "),font=(10))
Z_E = Entry(PV,width=8,font=(10))
cm10 = Label(PV,text=("cm"),font=(10))

X.grid(row=0,column=0)
X_E.grid(row=0,column=1)
cm8.grid(row=0,column=2)

Y.grid(row=1,column=0)
Y_E.grid(row=1,column=1)
cm9.grid(row=1,column=2)

Z.grid(row=2,column=0)
Z_E.grid(row=2,column=1)
cm10.grid(row=2,column=2)

# image frame
img = PhotoImage(file="SCARAV3.PNG")
img = img.subsample(1,2)
PI = Label(gui,image=img)
PI.grid(row=3,column=0)

gui.mainloop()