# BACHELOR OF SCIENCE IN MECHATRONICS ENGINEERING
## ROBOTICS 2: FINAL PROJECT
### Jacobian Matrix with Path and Trajectory Planning

---

### 📅 Important Dates

| Milestone | Date & Time | Venue |
| :--- | :--- | :--- |
| **Submission Date** | May 29, 2026, 11:59 PM | GitHub Repository |
| **Presentation Dates** | May 30 and May 31, 2026 | To Be Announced |

---

### 🎯 Objectives
By the end of this final project, students will be able to:
1. Upgrade and assemble the physical Spartan Robokit into a fully functional 5-Degree of Freedom (5-DOF) mechanical manipulator.
2. Formulate and mathematically derive the Jacobian Matrix to identify singularities and velocity relationships for the 5-DOF system.
3. Develop a Python-based computational tool to calculate the Jacobian Matrix accurately.
4. Implement precise industrial path and trajectory planning using the `jtraj` function within the MATLAB Robotics Toolbox.
5. Execute the planned trajectory by seamlessly integrating the MATLAB computational environment with the physical 5-DOF Spartan Robokit hardware.

---

### 🧰 Materials
1. Laptops
2. Visual Studio Code (VSCode) with Python extension
3. MATLAB with Robotics Toolbox by Peter Corke
4. Spartan Robokit (Upgraded to 5-DOF Hardware Configuration)

---

### 📋 Team Member Responsibilities & Instructions

#### 1. Project Engineer
* **Repository Setup:** Create a private GitHub repository for the group final project and add the lecturer as a collaborator.
* **Naming Convention:** Title the repository exactly as follows: 
  `Robotics2_Mechanical_Manipulator_Simulation_Section_Group#_FinalProject_2026`
* **Documentation:** Write these project instructions and procedures into the repository's `README.md` file.
* **Kinematics & Formatting:** * Draw the kinematic diagram with proper labels.
  * Construct the parametric table.
  * Derive the Homogeneous Transformation matrices.
  * Detail the final Jacobian Matrix derivation.
  * Upload and embed all pictures and mathematical derivations directly into the `README.md` file.
* **Data Integration:** Upload the final outputs, including pictures of the 5-DOF setup, source codes, and video demonstrations of the trajectory planning in action.
* **Team Support:** Assist the Project Leader in deriving and formally explaining the mathematical Jacobian Matrix solution for the Spartan Robokit.

#### 2. Programmer 1 (Python)
* **Scripting:** Build a dynamic Jacobian Matrix calculator in Python.
* **Parameters:** Strictly use the specific physical link lengths of the Spartan Robokit in your Python programs.
* **Defense Prep:** Prepare thoroughly for the Q&A portion regarding the step-by-step derivation of the formulae utilized in your program.
* **Submission:** Upload your completed Python program into a designated folder within the GitHub repository created by the Project Engineer.

#### 3. Programmer 2 (MATLAB & Hardware)
* **Hardware Upgrade:** Physically build and configure the Spartan Robokit into a 5-DOF manipulator.
* **Trajectory Planning:** Program the MATLAB Robotics Toolbox to compute and simulate the path and trajectory of the robot using the `jtraj` function. Ensure physical hardware constraints are strictly programmed and respected during this trajectory generation (e.g., verifying safe operational limits, such as 0° to 180° for joint variables like theta 2 and theta 3).
* **Integration & Execution:** Integrate the MATLAB toolbox to drive the actual 5-DOF robot along your calculated trajectory.
* **Submission:** Upload your completed MATLAB program into a designated folder within the GitHub repository created by the Project Engineer.

#### 4. Project Leader
* **Presentation Prep:** Prepare a strict **10-minute presentation** focused entirely on the derivation of the Jacobian Matrix solution for the Spartan Robokit. 
* **Execution:** You must use visual aids or a digital whiteboard to clearly explain the mathematical derivation, identifying potential singularities and velocity relationships to the panel.
* **Conclusion:** Deliver the final technical conclusion of the project, summarizing the success of the 5-DOF trajectory execution.

---

### 📊 Grading Rubric (Total: 70 Points)
*Assessment is based on the following Intended Learning Outcomes (ILOs):*

| Intended Learning Outcome (ILO) | Description | Points |
| :--- | :--- | :---: |
| **ILO1 (SO1)** | Calculate the Forward and Inverse Kinematics of robotic manipulators using D-H parameters and Graphical Methods. | **20 pts** |
| **ILO2 (SO5)** | Analyze robotic motion by computing the Jacobian Matrix to identify singularities and velocity relationships in 3-DOF and 5-DOF manipulators. | **40 pts** |
| **ILO4 (SO7)** | Present effective technical reports and design documentation through laboratory manuals and a professional portfolio website hosted on GitHub. | **10 pts** |
