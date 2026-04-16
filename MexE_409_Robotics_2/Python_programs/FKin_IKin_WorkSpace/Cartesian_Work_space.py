import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. Input the link lengths of the manipulator
# ==========================================
print("--- 1. Cartesian Link Lengths ---")
a1 = float(input("a1 = "))
a2 = float(input("a2 = "))
a3 = float(input("a3 = "))
a4 = float(input("a4 = "))

# ==========================================
# 2. Input the limits of d1, d2, and d3 (All Prismatic)
# ==========================================
print("\n--- 2. Joint Limits ---")
d1_min = float(input("d1 min (mm) = "))
d1_max = float(input("d1 max (mm) = "))
d2_min = float(input("d2 min (mm) = "))
d2_max = float(input("d2 max (mm) = "))
d3_min = float(input("d3 min (mm) = "))
d3_max = float(input("d3 max (mm) = "))

steps = 15
d1_vals = np.linspace(d1_min, d1_max, steps)
d2_vals = np.linspace(d2_min, d2_max, steps)
d3_vals = np.linspace(d3_min, d3_max, steps)

# ==========================================
# 3. Compute the workspace (UNIVERSAL SETUP)
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

# # Generation of position vectors using loops for Cartesian (d1, d2, d3)
for d1 in d1_vals:
    for d2 in d2_vals:
        for d3 in d3_vals:
            
            # Parametric Table for Cartesian (From your Cartesian_FKin.py)
            PT = [
                [0,               (270/180)*np.pi, 0, a1   ], 
                [(270/180)*np.pi, (270/180)*np.pi, 0, a2+d1], 
                [(90/180)*np.pi,  (270/180)*np.pi, 0, a3+d2],
                [0,               0,               0, a4+d3]
            ]
            
            # The universal function dynamically handles 4 rows now!
            H0_4 = compute_HTM(PT)
            
            X.append(H0_4[0][3])
            Y.append(H0_4[1][3])
            Z.append(H0_4[2][3])

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

# For Cartesian, the workspace will look like a solid floating Box/Cube
ax.scatter(X, Y, Z, c=Z, cmap='plasma', marker='s', s=2, alpha=0.5)

ax.set_title('Cartesian Manipulator Workspace Simulation')
ax.set_xlabel('X (mm)')
ax.set_ylabel('Y (mm)')
ax.set_zlabel('Z (mm)')
plt.show()

# ==========================================
# 6. Solve the Inverse Kinematics
# ==========================================
print("\n--- 6. Inverse Kinematics ---")
x0_4 = float(input("Target x0_4 = "))
y0_4 = float(input("Target y0_4 = "))
z0_4 = float(input("Target z0_4 = "))

# Inverse Kinematic Solutions (From your Cartesian_IKin.py)
d2_ans = x0_4 - a3
d3_ans = a1 - z0_4 - a4
d1_ans = y0_4 - a2

# --- REACHABILITY CHECK FOR CARTESIAN ---
# A Cartesian robot can only reach the target if the required joint movements 
# fall within the min and max limits
if not (d1_min <= d1_ans <= d1_max):
    print(f"\n[ERROR] Target is OUT OF BOUNDS on the Y-axis! Requires d1 = {d1_ans}, but limit is {d1_min} to {d1_max}.")
elif not (d2_min <= d2_ans <= d2_max):
    print(f"\n[ERROR] Target is OUT OF BOUNDS on the X-axis! Requires d2 = {d2_ans}, but limit is {d2_min} to {d2_max}.")
elif not (d3_min <= d3_ans <= d3_max):
    print(f"\n[ERROR] Target is OUT OF BOUNDS on the Z-axis! Requires d3 = {d3_ans}, but limit is {d3_min} to {d3_max}.")
else:
    # ==========================================
    # 7. Print the joint variables
    # ==========================================
    print("\n--- 7. Joint Variables ---")
    print("d1 = ", np.around(d1_ans, 3))
    print("d2 = ", np.around(d2_ans, 3))
    print("d3 = ", np.around(d3_ans, 3))