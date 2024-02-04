disp('Cylindrical Manipulator')
syms a1 a2 a3 t1 d2 d3

%% Link lengths
a1 = 3;
a2 = 3;
a3 = 3;

%% Joint Variables
d2 = 2;
d3 = 2;

%% D-H Parameters [theta, d, r, alpha, offset]
% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint: theta = 0,offset = 0, after offset put the value of theta
H0_1 = Link([0,a1,0,0,0,0]);
H0_1.qlim = [-pi/2 pi/2];

H1_2 = Link([3*pi/2,0,0,3*pi/2,1,a2]);
H1_2.qlim = [0 d2];

H2_3 = Link([0,0,0,0,1,a3]);
H2_3.qlim = [0 d3];

Cyl = SerialLink([H0_1 H1_2 H2_3], 'name', 'Cyl')
Cyl.plot([0 0 0], 'workspace', [-5 8 -8 8 0 9])
Cyl.teach