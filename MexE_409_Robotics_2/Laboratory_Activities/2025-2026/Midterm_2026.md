# BACHELOR OF SCIENCE IN MECHATRONICS ENGINEERING
## ROBOTICS 2: Midterm Project

# Title: Inverse Kinematics

### 📅 Important Dates

**Submission Dates:**
* **MEXE-3203/04:** April 24, 2026, 11:59 PM
* **MEXE-3201 & 3202:** April 25, 2026, 11:59 PM

**Presentation Dates:**
* **MEXE-3203/04:** April 26, 2026
* **MEXE-3201 & 3202:** April 26, 2026

---

## 🎯 Objectives
1. **Derive and Apply Inverse Kinematics:** To mathematically derive the Inverse Kinematics (IK) solutions for a 3-DOF Spartan Robokit using the Graphical Method and Denavit-Hartenberg (D-H) parameters.
2. **Develop Computational Tools:** To program a robust Python-based calculator capable of solving both Forward and Inverse Kinematics, as well as simulating the 3D workspace of the manipulator.
3. **Digital Twin Integration:** To bridge the gap between simulation and reality by controlling the physical Spartan Robokit using a Digital Twin model, validating coordinate mapping and joint variables.
4. **Physical Validation:** To practically test the computed Inverse Kinematics through physical pick-and-place tasks using specific 3D Cartesian coordinates (X, Y, Z).
5. **System Analysis:** To analyze and classify the kinematic outputs of the robot (Correct IK, FK = IK, Mirror, or Undefined) across multiple test points.

---

## 🛠️ Materials
* Laptops
* VSCode with Python
* MATLAB with Robotics Toolbox by Peter Corke
* Spartan Robokit

---

## 👥 Roles and Responsibilities

### 👷‍♂️ Project Engineer
- [ ] Create the group laboratory repository, set it to **Private**, and add the instructor as a collaborator. 
  * *Repository Naming Convention:* `Robotics2_Mechanical_Manipulator_Simulation_Section_Group#_MidtermProject_2026`
- [ ] Write the laboratory instructions and procedures in this GitHub repository's `README.md` file.
- [ ] Draw the Kinematic Diagram (with labels), the Parametric (D-H) Table, and the Homogeneous Transformation Matrices (HTM) of the Spartan Robokit. Upload and display these images in the Kinematics section of this `README.md`.
- [ ] Post the outputs and documentation (pictures, codes, and videos) in the repository:
  - [ ] Post a side-by-side video comparing the controlled Digital Twin and the physical robot being driven by the Digital Twin (Execute the 5-point position vector test).
  - [ ] Evaluate the 5 test points and classify the Inverse Kinematics outputs as: **a.** Correct IK, **b.** FK = IK, **c.** Mirror, or **d.** Undefined.
- [ ] Assist the Project Leader in deriving and explaining the Inverse Kinematics solutions for the Spartan Robokit.

### 💻 Programmer 1
- [ ] Build the Inverse Kinematics and Workspace Python calculator.
- [ ] Ensure the exact link lengths of the physical Spartan Robokit are used in the Python programs.
- [ ] Prepare for the Q&A session regarding the derivation of the mathematical formulas used in the Python code.
- [ ] Upload the final program into a designated folder inside this repository.

### 💻 Programmer 2
- [ ] Modify the Forward Kinematics program from the Prelim project to solve *both* Forward and Inverse Kinematics.
- [ ] Integrate the Inverse Kinematics program with the physical Spartan Robokit. 
- [ ] Conduct a 5-point test (using 5 different sets of target position vectors). Use the attached Excel file as a checklist for these points.
- [ ] Perform a physical pick-and-place test using the Inverse Kinematics method. **Note:** Use a ruler or measuring tape during execution to verify coordinates. Ensure this measurement process is clearly visible in the recorded video.
- [ ] Upload the integration script into a designated folder inside this repository.

### 🗣️ Project Leader
- [ ] Prepare a 10-minute presentation explaining the derivation of the Inverse Kinematics solutions for the Spartan Robokit. *(You may use markers and rulers or a digital whiteboard during the explanation).*
- [ ] Write and present the final Conclusion of the project.

---

## 📊 Kinematic Modeling
> *(Project Engineer: Replace these placeholders with the actual images of your derivations)*

### 1. Kinematic Diagram
*[Insert Kinematic Diagram Image Here]*

### 2. Parametric (D-H) Table
*[Insert D-H Table Image Here]*

### 3. Homogeneous Transformation Matrices (HTM)
*[Insert HTM Equations Image Here]*

---

## 🎥 Documentation and Media
> *(Project Engineer: Insert your side-by-side videos, pick-and-place demonstration, and the 5-point test evaluation here)*

* **Digital Twin vs. Physical Robot Video:** [Insert Link or GIF]
* **Pick and Place Execution:** [Insert Link or GIF]
* **5-Point Test Evaluation Results:**
  * Point 1: `[Result Classification]`
  * Point 2: `[Result Classification]`
  * Point 3: `[Result Classification]`
  * Point 4: `[Result Classification]`
  * Point 5: `[Result Classification]`

---

## 📝 Conclusion
> *(Project Leader: Write the final conclusion of the project here based on the experimental results, accuracy of the IK, and the performance of the Spartan Robokit).*

---

## 🏆 Grading Rubric
Grades will be evaluated based on the following Intended Learning Outcomes (ILOs):

| ILO | Description | SO Alignment | Points |
| :--- | :--- | :---: | :---: |
| **ILO1** | Calculate the Forward and Inverse Kinematics of 3-DOF robotic manipulators using D-H parameters and Graphical Methods. | **SO1** | 20 pts |
| **ILO2** | Analyze robotic motion by computing the Jacobian Matrix to identify singularities and velocity relationships in 3-DOF and 6-DOF manipulators. | **SO5** | 40 pts |
| **ILO4** | Present effective technical reports and design documentation through laboratory manuals and a professional portfolio website hosted on GitHub. | **SO7** | 10 pts |
| | | **TOTAL** | **70 pts** |
