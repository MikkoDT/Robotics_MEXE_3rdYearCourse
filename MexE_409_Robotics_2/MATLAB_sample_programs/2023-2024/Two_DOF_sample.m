%Parametric D-H:
syms a1 a2 
a1=3
a2=3

L1 = Link([0,a1,0,pi/2,0])
L1.qlim =  pi/180*[-90 90]
L2 = Link([0,0,a2,0,0])
L2.qlim =  pi/180*[-90 90]

TwoDOF = SerialLink([ L1 L2 ], 'name', 'TwoDOF')
TwoDOF.plot([0 0], 'workspace' , [-7 7 -7 7 -7 7])
TwoDOF.fkine([30 40], 'deg')

