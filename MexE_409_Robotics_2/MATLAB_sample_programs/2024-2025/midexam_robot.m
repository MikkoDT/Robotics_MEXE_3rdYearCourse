clear all
clc
close all

disp('Midterm Exam - Test 3')

%% Link lenths
a1 = 20;
a2 = 10;
a3 = 10;
a4 = 5;

%% D-H Parameters [theta, d, r, alpha, offset]
% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint: theta = 0,offset = 0, after offset put the value of theta

H0_1 = Link([0,0,0,pi/2,1,-a1]);
H0_1.qlim = [0 0];

H1_2 = Link([0,0,0,0,1,a2]);
H1_2.qlim = [0 5];

H2_3 = Link([0,0,a3,pi/2,0,0]);
H2_3.qlim = [-pi/2 pi/2];

H3_4 = Link([0,0,0,0,1,a4]);
H3_4.qlim = [0 5];

Mid3 = SerialLink([H0_1 H1_2 H2_3 H3_4], 'name', 'Test3')
Mid3.plot([0 0 0 0], 'workspace', [-8 18 -18 18 -36 0])

figure(1)
Mid3.teach