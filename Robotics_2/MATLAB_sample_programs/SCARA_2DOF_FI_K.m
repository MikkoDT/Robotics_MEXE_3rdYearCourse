disp('SCARA 2DOF')
syms a1 a2 a3 a4 t1 t2

%% Link lengths
a1=3;
a2=3;
a3=3;
a4=3;

%% D-H Parameters [theta, d, r, alpha, offset]
% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint: theta = 0,offset = 0, after offset put the value of theta
H0_1 = Link([0,a1,a2,0,0,0]);
H0_1.qlim = [-pi/2 pi/2];

H1_2 = Link([0,a3,a4,0,0,0]);
H1_2.qlim = [-pi/2 pi/2];

S_2DOF =SerialLink([H0_1 H1_2], 'name', 'Practice 3')
S_2DOF.plot([0 0], 'workspace' , [-5 10 -10 10 0 10])
S_2DOF.teach

%% Forward Kinematics
fkin = [0 0];
F_Kin = S_2DOF.fkine(fkin)

fkin_1 = [pi/2 -pi/2]
F_Kin_1 = S_2DOF.fkine(fkin_1)

% qready = [0 0 0];
% T=transl([1.5,5.598,6]);
% q=P3.ikine(T,qready, 'mask', [1 1 0 0 0 0])