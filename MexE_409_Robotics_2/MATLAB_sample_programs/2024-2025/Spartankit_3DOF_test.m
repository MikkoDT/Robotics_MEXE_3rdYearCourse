%Clear
clear
clc
close all

disp('Spartankit')
syms a1 a2 a3

%% Link lengths
a1 = 6;
a2 = 5;
a3 = 4;

%% D-H Parameters [theta, d, r, alpha, offset]
% if prismatic joint: theta = theta, d = 0, offset = 1, after offset put the value of d
% if revolute joint: theta = 0,offset = 0, after offset put the value of theta

H0_1 = Link([0,a1,0,pi/2,0,0]);
H0_1.qlim = [-90 90];

H1_2 = Link([0,0,a2,0,0,pi/2]);
H1_2.qlim = pi/180*[-90 90];

H2_3 = Link([0,0,a3,0,0,0]);
H2_3.qlim = pi/180*[-90 90];

Spart = SerialLink([H0_1 H1_2 H2_3], 'name', 'Spartankit')
Spart.plot([0 0 0], 'workspace', [-3 15 -15 15 0 15])

figure(1)
Spart.teach