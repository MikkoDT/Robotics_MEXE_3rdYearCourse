disp('SCARA_V3')
syms a1 a2 a3 a4

%% Link lengths
a1 = 20;
a2 = 30;
a3 = 10;
a4 = 15;

%% D-H Parameters [theta, d, r, alpha, offset]
% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint: theta = 0,offset = 0, after offset put the value of theta

H0_1 = Link([0,0,0,0,1,a1]);
H0_1.qlim = [0 30];

H1_2 = Link([0,0,a2,0,0]);
H1_2.qlim = pi/180*[-90 90];

H2_3 = Link([0,a3,a4,0,0]);
H2_3.qlim = pi/180*[-90 90];

Scara_V3 = SerialLink([H0_1 H1_2 H2_3], 'name', 'SCARA_V3')
Scara_V3.plot([0 0 0], 'workspace', [-10 75 -80 80 0 80])
Scara_V3.teach

%% Forward Kinemtics
%syntax: FK = robot_variable.fkine(joint_variables)
Af = ([5,pi/2,pi/2]); %joint_variables
FK = Scara_V3.fkine(Af)

%% Inverse Kinematics
%syntax: IK = robot_variable.ikine(PV,qready,'mask',[1 1 1 0 0 0])
q_init=[0 0 0];
PV=transl([-15 30 35]);
IK = Scara_V3.ikine(PV,q_init,'mask',[1 1 1 0 0 0])