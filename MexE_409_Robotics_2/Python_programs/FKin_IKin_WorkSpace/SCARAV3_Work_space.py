import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Input the link lengths of the manipulator
# ==========================================
print("--- 1. Link Lengths ---")
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))

# ==========================================
# 2. Input the limits of d1, theta2, and theta3
# ==========================================
print("\n--- 2. Joint Limits ---")
d1_min = float(input("d1 min (mm) = "))
d1_max = float(input("d1 max (mm) = "))
T2_min = float(input("T2 min (deg) = "))
T2_max = float(input("T2 max (deg) = "))
T3_min = float(input("T3 min (deg) = "))
T3_max = float(input("T3 max (deg) = "))

# steps=19 ensures it hits exactly 0, 10, 20... 90... 180 degrees
steps = 19
d1_vals = np.linspace(d1_min, d1_max, steps)
T2_vals = np.linspace(T2_min, T2_max, steps)
T3_vals = np.linspace(T3_min, T3_max, steps)

# ==========================================
# 3. Compute the workspace (Universal Setup)
# ==========================================
print("\n--- 3. Computing Workspace ---")

def compute_HTM(PT):
    H_total = np.eye(4)
    for i in range(len(PT)):
        theta = PT[i][0]
        alpha = PT[i][1]
        r     = PT[i][2]
        d     = PT[i][3]
        
        H = np.array([
            [np.cos(theta), -np.sin(theta)*np.cos(alpha),  np.sin(theta)*np.sin(alpha), r*np.cos(theta)],
            [np.sin(theta),  np.cos(theta)*np.cos(alpha), -np.cos(theta)*np.sin(alpha), r*np.sin(theta)],
            [0,              np.sin(alpha),               np.cos(alpha),               d              ],
            [0,              0,                           0,                           1              ]
        ])
        H_total = np.dot(H_total, H)
    return H_total

X = []
Y = []
Z = []

# Generation of position vectors using loops
for d1 in d1_vals:
    for T2 in T2_vals:
        for T3 in T3_vals:
            t2_rad = (T2/180)*np.pi
            t3_rad = (T3/180)*np.pi
            
            # Parametric Table for SCARA-V3
            PT = [[(0/180)*np.pi, (0/180)*np.pi, 0,  a1+d1],
                [t2_rad,        (0/180)*np.pi, a2, 0    ],
                [t3_rad,        (0/180)*np.pi, a4, a3   ]]
            
            H0_3 = compute_HTM(PT)
            
            X.append(H0_3[0][3])
            Y.append(H0_3[1][3])
            Z.append(H0_3[2][3])

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

# ==========================================
# 4. Print the limits of the position vectors
# ==========================================
print("\n--- 4. Position Vector Limits ---")
print("x limits: ", np.around(np.min(X), 3), "to", np.around(np.max(X), 3))
print("y limits: ", np.around(np.min(Y), 3), "to", np.around(np.max(Y), 3))
print("z limits: ", np.around(np.min(Z), 3), "to", np.around(np.max(Z), 3))

# ==========================================
# 5. Simulate the workspace
# ==========================================
print("\n--- 5. Simulating Workspace ---")
print("NOTE: Close the 3D plot window to continue to Inverse Kinematics.")

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X, Y, Z, c=Z, cmap='jet', marker='o', s=2, alpha=0.5)

ax.set_title('SCARA-V3 Workspace Simulation')
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
plt.show()

# ==========================================
# 6. Solve the Inverse Kinematics
# ==========================================
print("\n--- 6. Inverse Kinematics ---")
x0_3 = float(input("x0_3 = "))
y0_3 = float(input("y0_3 = "))
z0_3 = float(input("z0_3 = "))

# --- REACHABILITY CHECK ---
r1 = np.sqrt((y0_3**2) + (x0_3**2))
max_reach = a2 + a4

if r1 > max_reach:
    print(f"\n[ERROR] Target is OUT OF BOUNDS!")
    print(f"Maximum reach in XY plane is {max_reach} mm, but your target is {np.around(r1,3)} mm away.")
else:
    # Quick fix for division by zero in your specific arctan formula
    if x0_3 == 0:
        x0_3 = 0.00001 

    # Inverse Kinematic Solutions using Graphical Method
    # Solution 1
    phi2 = np.arctan(y0_3/x0_3)
    phi2 = phi2*180/np.pi

    # Solution 2 (already calculated above as r1)

    # Solution 3
    phi1 = np.arccos((a4**2-r1**2-a2**2)/(-2*r1*a2))
    phi1 = phi1*180/np.pi

    # Solution 4
    theta2 = phi2 - phi1

    # Solution 5
    phi3 = np.arccos((r1**2-a2**2-a4**2)/(-2*a2*a4))
    phi3 = phi3*180/np.pi

    # Solution 6
    theta3 = 180 - phi3

    # Solution 7
    d1 = z0_3 - a1 - a3

    # ==========================================
    # 7. Print the joint variables
    # ==========================================
    print("\n--- 7. Joint Variables ---")
    print("d1 = ", np.around(d1, 3))
    print("theta2 = ", np.around(theta2, 3))
    print("theta3 = ", np.around(theta3, 3))