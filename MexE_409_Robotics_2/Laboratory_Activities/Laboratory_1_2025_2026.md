# BACHELOR OF SCIENCE IN MECHATRONICS ENGINEERING
## ROBOTICS 2: LABORATORY 1
### Python and Robotics Toolbox Mechanical Manipulator Simulation

---

### 📅 Important Dates

| Section | Submission Date | Presentation Date & Venue |
| :--- | :--- | :--- |
| **MEXE 3203 / 3204** | February 26, 2026, 11:59 PM | February 27, 2026, 7:00 AM (Online) |
| **MEXE 32101 & 3202** | February 28, 2026, 11:59 PM | February 28, 2026, 5:00 PM (Online) |

---

### 🎯 Objectives
By the end of this laboratory experiment, students will be able to:
1. Formulate the kinematic model of an assigned mechanical manipulator using Denavit-Hartenberg (D-H) parameters and graphical methods.
2. Develop and execute forward kinematics simulations using both Python and MATLAB (Robotics Toolbox by Peter Corke).
3. Validate simulation accuracy by cross-verifying computational outputs from both software environments across multiple joint variable test points.
4. Present technical findings effectively through professional documentation and a structured oral defense.

---

### 🧰 Materials
1. Laptops
2. Visual Studio Code (VSCode) with Python extension
3. MATLAB with Robotics Toolbox by Peter Corke

---

### 📋 Team Member Responsibilities & Instructions

#### 1. Project Engineer
* **Repository Setup:** Create the group laboratory repository on GitHub. **Ensure the repository is set to Private** and add the lecturer as a collaborator.
* **Naming Convention:** Title the repository exactly as follows: 
  `Robotics2_Mechanical_Manipulator_Simulation_Section_Group#_Laboratory1_2026`
* **Documentation:** Write these laboratory instructions and procedures into the repository's `README.md` file.
* **Kinematics & Formatting:** * Draw the kinematic diagram with proper labels.
  * Construct the parametric table.
  * Derive the Homogeneous Transformation matrices of the mechanical manipulator assigned to your group.
  * Upload and post the pictures directly in the GitHub ReadMe file.
* **Manipulator Link Format:** Use the following format to link your assigned manipulator references:
  > **Assigned Manipulator:** [Insert Manipulator Name/Model]  
  > **Reference Link:** [Click here to view documentation](Insert URL Here)
* **Data Integration:** Post the simulations and the analytical comparisons of the Python and MATLAB findings.

#### 2. Programmer 1 (Python)
* **Scripting:** Program the assigned mechanical manipulator in Python using the codes your lecturer taught you.
* **Parameters:** Assign only **one** set of link lengths.
* **Testing:** Test **5 test points**, meaning 5 different sets of values for joint variables.
* **Submission:** Post your program in a folder inside the repository created by your Project Engineer.

#### 3. Programmer 2 (MATLAB)
* **Scripting:** Program the assigned mechanical manipulator in MATLAB with Robotics Toolbox by Peter Corke using the codes your lecturer taught you.
* **Parameters:** Assign only **one** set of link lengths.
* **Testing:** Test **5 test points**, meaning 5 different sets of values for joint variables.
* **Submission:** Post your program in a folder inside the repository created by your Project Engineer.

#### 4. Project Leader
* **Presentation Prep:** Prepare a **10-minute presentation** of the laboratory. (Strictly 10 minutes only).
* **Presentation Content:** You will present the following:
  1. The kinematic diagram with labels, parametric table, and Homogeneous Transformation matrices of the mechanical manipulator assigned to your group.
  2. The simulation and comparison of the 2 simulations.
  3. Verification of how the simulations are correct (Based on what I taught).
  4. Conclusion.
* **Defense Coordination:** For the other 3 members, prepare them for the **5-minute question and answer** portion.

---

### 📝 Standard D-H Transformation Matrix Reference
*Students: Utilize the standard Denavit-Hartenberg transformation matrix for your calculations:*

```text
[ cos(θn)  -sin(θn)cos(αn)   sin(θn)sin(αn)  rn*cos(θn) ]
[ sin(θn)   cos(θn)cos(αn)  -cos(θn)sin(αn)  rn*sin(θn) ]
[   0         sin(αn)          cos(αn)          dn      ]
[   0            0                0              1      ]
```


### Reference Grading Rubric (Total: 60 Points)
| Intended Learning Outcome (ILO) | Description | Points |
| :--- | :--- | :---: |
| **ILO1 (SO1)** | Calculate the Forward and Inverse Kinematics of 3-DOF robotic manipulators using D-H parameters and Graphical Methods. | 5 pts |
| **ILO2 (SO5)** | Analyze robotic motion by computing the Jacobian Matrix to identify singularities and velocity relationships in 3-DOF and 6-DOF manipulators. | 10 pts |
| **ILO3 (SO11)** | Utilize modern engineering tools, such as Python, MATLAB, and Arduino, to implement trajectory planning and simulate robotic control systems. | 25 pts |
| **ILO4 (SO7)** | Present effective technical reports and design documentation through laboratory manuals and a professional portfolio website hosted on GitHub. | 20 pts |
