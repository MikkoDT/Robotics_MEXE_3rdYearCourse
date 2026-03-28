# BACHELOR OF SCIENCE IN MECHATRONICS ENGINEERING
## ROBOTICS 2: LABORATORY 1
### Python and Robotics Toolbox Mechanical Manipulator Simulation

---

### 📅 Important Dates

| Section | Submission Date | Presentation Date & Venue |
| :--- | :--- | :--- |
| **MEXE 3201 & 3202 & 3203 / 3204** | February 28, 2026, 11:59 PM | March 1, 2026 (Face to Face) |

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
* **Manipulator Link:** 
  > **Assigned Manipulator:** [https://github.com/MikkoDT/Robotics_MEXE_3rdYearCourse/blob/main/MexE_409_Robotics_2/Laboratory_Activities/Laboratory_1_Mechanical_Manipulators.pdf]  
 
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

### Detailed Grading Matrix (60 Points Total)

| Intended Learning Outcome (ILO) | Exceptional (100%-95%) | Exemplary (94%-85%) | Proficient (84%-75%) | Competent (74%-65%) | Developing (64%-55%) | Needs Improvement (54%-50%) | Poor/Missing (< 50%) | Max Points |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **ILO1: Kinematics (5 pts)** | Flawless diagram, D-H table, and matrices. | Minor labeling error, perfect matrices and D-H. | Minor arithmetic errors in matrices, correct D-H. | Some incorrect D-H parameters affecting matrices. | Major errors in D-H parameter extraction. | Matrices and parameters are mostly incorrect. | Missing or fundamentally flawed. | **5** |
| **ILO2: Analysis (10 pts)** | Flawless Jacobian & singularity analysis for *both* 3-DOF and 6-DOF. | Accurate Jacobian, but misses minor singularities in 6-DOF. | Minor math errors in either the 3-DOF or 6-DOF analysis. | Completes 3-DOF perfectly, struggles heavily with 6-DOF. | Completes analysis for 3-DOF only; missing 6-DOF. | Major conceptual errors in the 3-DOF analysis. | Fails to compute Jacobian or analyze motion. | **10** |
| **ILO3: Simulation (25 pts)** | Flawless Python/MATLAB execution for *both* 3-DOF and 6-DOF. | Codes run flawlessly for both, minor variable naming issues. | Codes run for both but have slight output discrepancies. | Successful 3-DOF simulation, 6-DOF has major logical errors. | Fails to build 6-DOF completely; 3-DOF has minor bugs. | Significant bugs in both languages; fails to execute properly. | Programs fail to run; missing either Python or MATLAB. | **25** |
| **ILO4: Presentation (20 pts)** | Perfect repository. Strict 10-min presentation, strong math verification, flawless Q&A. | Great repository. Presentation is clear but slightly off timing, good Q&A. | Good repo but missing formatting. Weak math verification. | Disorganized repository. Presentation flow is poor, struggles in Q&A. | Unorganized repo. Exceeds time limits significantly. | Very poor presentation and unable to answer Q&A. | Repo not submitted or presentation unprepared. | **20** |
