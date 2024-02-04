disp('SCARA 2DOF')
syms a1 a2 a3 a4 a5 t1 t2 d3

%% Link lengths
a1 = 4;
a2 = 3;
a3 = 4;
a4 = 3;
a5 = 3;

%% Joint Variables
d3 = 4;

%% D-H Parameters [theta, d, r, alpha, offset]
% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint: theta = 0,offset = 0, after offset put the value of theta
H0_1 = Link([0,a1,a2,0,0,0]);
H0_1.qlim = [-pi/2 pi/2];

H1_2 = Link([0,a3,a4,pi,0,0]);
H1_2.qlim = [-pi/2 pi/2];

H2_3 = Link([0,0,0,0,1,a5]);
H2_3.qlim = [0 d3];

SCARA = SerialLink([H0_1 H1_2 H2_3], 'name', 'SCARA')
SCARA.plot([0 0 0], 'workspace', [-3 12 -11 11 -3 10])
SCARA.teach