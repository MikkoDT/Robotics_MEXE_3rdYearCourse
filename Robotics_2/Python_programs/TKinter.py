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

# Create GUI window with title
mygui = Tk()
mygui.title("SCARAV3 Calculator")
mygui.resizable(False,False)
mygui.configure(bg="pink")

def reset():
        a1_E.delete(0, END)
        a2_E.delete(0, END)
        a3_E.delete(0, END)
        a4_E.delete(0, END)

        d1_E.delete(0, END)
        T2_E.delete(0, END)
        T3_E.delete(0, END)

        X_E.delete(0, END)
        Y_E.delete(0, END)
        Z_E.delete(0, END)

def f_k():
    # link lengths in cm
        a1 = float(a1_E.get())/100
        a2 = float(a2_E.get())/100
        a3 = float(a3_E.get())/100
        a4 = float(a4_E.get())/100

    # joint variables: if d cm, if Theta degrees
        d1 = float(d1_E.get())/100
        T2 = float(T2_E.get())
        T3 = float(T3_E.get())

    # degrees to radian
        T2 = (T2/180.0)*np.pi
        T3 = (T3/180.0)*np.pi

    # Parametric Table (Theta, alpha, r, d)
        PT = [[(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,0,a1+d1],
         [T2,(0.0/180.0)*np.pi,a2,0],
         [T3,(0.0/180.0)*np.pi,a4,a3]]

    # HTM Formulae
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

        H0_1 = np.matrix(H0_1)

        H1_2 = np.matrix(H1_2)

        H2_3 = np.matrix(H2_3)

        H0_2 = np.dot(H0_1,H1_2)
        H0_3 = np.dot(H0_2,H2_3)

        X0_3 = H0_3[0,3]
        X_E.delete(0,END)
        X_E.insert(0,np.around(X0_3*100,3))

        Y0_3 = H0_3[1,3]
        Y_E.delete(0,END)
        Y_E.insert(0,np.around(Y0_3*100,3))

        Z0_3 = H0_3[2,3]
        Z_E.delete(0,END)
        Z_E.insert(0,np.around(Z0_3*100,3))

    # Create links
    # [robot_variable]=DHRobot([RevoluteDH(d,r,alpha,offset)])
        SCARA_V3 = DHRobot([
                PrismaticDH(0,0,(0.0/180.0)*np.pi,a1,qlim=[0,(30/100)]),
                RevoluteDH(0,a2,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
                RevoluteDH(a3,0,(0.0/180.0)*np.pi,(0.0/180.0)*np.pi,qlim=[-np.pi/2,np.pi/2]),
                PrismaticDH(0,a4,0,0,qlim=[0,0])
                ], name='SCARA_V3')

        # plot joints
        q1 = np.array([d1,T2,T3,0])

        # plot scale
        x1 = -0.8
        x2 = 0.8
        y1 = -0.8
        y2 = 0.8
        z1 = 0
        z2 = 0.8

        # Plot command
        SCARA_V3.plot(q1,limits=[x1,x2,y1,y2,z1,z2],block=True)

# Link lengths and Joint variable Frame
FI = LabelFrame(mygui,text="Link Lengths and Joint Variables",font=(5))
FI.grid(row=0,column=0)

# Link lengths label
a1 = Label(FI,text=("a1 = "),font=(10),bg="brown")
a1_E = Entry(FI,width=5,font=(10),bg="purple")
cm1 = Label(FI,text=("cm "),font=(10),bg="brown")

a2 = Label(FI,text=("a2 = "),font=(10),bg="brown")
a2_E = Entry(FI,width=5,font=(10))
cm2 = Label(FI,text=("cm "),font=(10),bg="brown")

a3 = Label(FI,text=("a3 = "),font=(10),bg="brown")
a3_E = Entry(FI,width=5,font=(10))
cm3 = Label(FI,text=("cm "),font=(10),bg="brown")

a4 = Label(FI,text=("a4 = "),font=(10),bg="brown")
a4_E = Entry(FI,width=5,font=(10))
cm4 = Label(FI,text=("cm  "),font=(10),bg="brown")

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

# Joint variables label
d1 = Label(FI,text=("d1 = "),font=(10))
d1_E = Entry(FI,width=5,font=(10))
cm5 = Label(FI,text=("cm"),font=(10))

T2 = Label(FI,text=("T2 = "),font=(10))
T2_E = Entry(FI,width=5,font=(10))
deg1 = Label(FI,text=("deg"),font=(10))

T3 = Label(FI,text=("T3 = "),font=(10))
T3_E = Entry(FI,width=5,font=(10))
deg2 = Label(FI,text=("deg"),font=(10))

d1.grid(row=0,column=3)
d1_E.grid(row=0,column=4)
cm5.grid(row=0,column=5)

T2.grid(row=1,column=3)
T2_E.grid(row=1,column=4)
deg1.grid(row=1,column=5)

T3.grid(row=2,column=3)
T3_E.grid(row=2,column=4)
deg2.grid(row=2,column=5)

# Buttons Frame
BF = LabelFrame(mygui,text="Forward Kinematics",font=(5),bg="indigo",fg="yellow")
BF.grid(row=1,column=0)

# Buttons
FK = Button(BF,text="Forward",font=(10),bg="blue",fg="white",command=f_k)
rst = Button(BF,text="RESET",font=(10),bg="red",fg="white",command=reset)

FK.grid(row=0,column=0)
rst.grid(row=0,column=1)

# Position Vectors Frame
PV = LabelFrame(mygui,text="Position Vectors",font=(5))
PV.grid(row=2,column=0)

# Position Vectors label
X = Label(PV,text=("X = "),font=(10))
X_E = Entry(PV,width=5,font=(10))
cm6 = Label(PV,text=("cm"),font=(10))

Y = Label(PV,text=("Y = "),font=(10))
Y_E = Entry(PV,width=5,font=(10))
cm7 = Label(PV,text=("cm"),font=(10))

Z = Label(PV,text=("Z = "),font=(10))
Z_E = Entry(PV,width=5,font=(10))
cm8 = Label(PV,text=("cm"),font=(10))

X.grid(row=0,column=0)
X_E.grid(row=0,column=1)
cm6.grid(row=0,column=2)

Y.grid(row=1,column=0)
Y_E.grid(row=1,column=1)
cm7.grid(row=1,column=2)

Z.grid(row=2,column=0)
Z_E.grid(row=2,column=1)
cm8.grid(row=2,column=2)

# insert image
img = PhotoImage(file="SCARAV3.PNG")
img = img.subsample(1,2)
PI = Label(mygui,image=img)
PI.grid(row=3,column=0)

mygui.mainloop()
