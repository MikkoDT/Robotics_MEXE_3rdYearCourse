%Clear
clear
clc
close all

disp('SCARA_V3')
syms a1 a2 a3 a4

%% Link lengths
a1 = 55;
a2 = 60;
a3 = 30;
a4 = 60;

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
Scara_V3.plot([0 0 0], 'workspace', [-120 120 -120 120 0 120])

figure(1)
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

%% Jacobian Matrix
q_j1 = [30 pi/2 -pi/18]
J1 = jacob0(Scara_V3,q_j1)

q_j2 = [10 27*pi/180 5*pi/18]
J2 = jacob0(Scara_V3,q_j2)

%% Path and Trajetory
t = 0:0.5:2

%q paths
q0 = [0 0 0];
q1 = [25 -pi/18 -pi/6];
q2 = [10 pi/6 pi/3];
q3 = [0 0 0];
q4 = [25 -pi/18 -pi/6];
q5 = [10 pi/6 pi/3];

% Trajectory
Traj1 = jtraj(q0,q1,t)
Traj2 = jtraj(q1,q2,t)
Traj3 = jtraj(q2,q3,t)
Traj4 = jtraj(q4,q5,t)
Traj5 = jtraj(q5,q0,t)

figure(2)
plot(Scara_V3,Traj1)
plot(Scara_V3,Traj2)
plot(Scara_V3,Traj3)
plot(Scara_V3,Traj4)
plot(Scara_V3,Traj5)
