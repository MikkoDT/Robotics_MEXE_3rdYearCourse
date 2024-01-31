% KD_DHF_3

disp('Practice 3')

syms a1 a2 a3 a4 t1 t2
a1=3;
a2=3;
a3=3;
a4=3;

L1 = Link([0,a1,a2,0]);
L1.qlim = pi/180*[-90 90];
L2 = Link([0,a3,a4,0]);
L2.qlim = pi/180*[-90 90];

P3=SerialLink([L1 L2], 'name', 'Practice 3');
P3.plot([0 0], 'workspace' , [-10 10 -10 10 -10 10]);
P3.teach;
qf = [0 0];
Tf = P3.fkine(qf)
qready = [0 0 0];
T=transl([1.5,5.598,6]);
q=P3.ikine(T,qready, 'mask', [1 1 0 0 0 0])