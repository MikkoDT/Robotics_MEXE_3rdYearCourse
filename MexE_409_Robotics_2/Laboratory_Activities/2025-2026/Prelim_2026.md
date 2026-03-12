# BACHELOR OF SCIENCE IN MECHATRONICS ENGINEERING
## ROBOTICS 2: PRELIMINARY PROJECT
### Forward Kinematics

---

### 📅 Important Dates

| Milestone | Date & Time | Venue |
| :--- | :--- | :--- |
| **Submission Date** | March 28, 2026, 11:59 PM | GitHub Repository |
| **Presentation Date** | March 29, 2026 | To Be Announced |

---

### 🎯 Objectives
By the end of this preliminary project, students will be able to:
1. Derive the kinematic model of the Spartan Robokit using Denavit-Hartenberg (D-H) parameters and graphical methods.
2. Successfully interface MATLAB with an Arduino-driven microcontroller based on the framework established by Balabag et al.
3. Translate theoretical forward kinematics into physical robotic motion by testing multiple joint variable configurations.
4. Execute a practical pick-and-place operation utilizing the programmed forward kinematics model.
5. Document physical circuitry, software integration, and mechanical assembly in a professional technical repository.

---

### 🧰 Materials
1. Laptops
2. MATLAB with Robotics Toolbox by Peter Corke
3. Spartan Robokit (Hardware & Circuitry)

---

### 📋 Team Member Responsibilities & Instructions

#### 1. Project Engineer
* **Repository Setup:** Create a private GitHub repository for the group project and add the lecturer as a collaborator.
* **Naming Convention:** Title the repository exactly as follows: 
  `Robotics2_Mechanical_Manipulator_Simulation_Section_Group#_PrelimProject_2026`
* **Documentation:** Write these project instructions and procedures into the repository's `README.md` file.
* **Kinematics & Formatting:** * Draw the kinematic diagram with proper labels for the Spartan Robokit.
  * Construct the parametric table.
  * Derive the Homogeneous Transformation matrices.
  * Upload and embed these images directly into the `README.md` file.
* **Data Integration:** Upload and organize the final project documentation, including pictures of the setup, source codes, and video demonstrations of the robot in motion.

#### 2. Programmer 1 & Programmer 2
* **Software Integration:** Study, analyze, and apply the existing program by Balabag et al. to successfully integrate MATLAB with the Arduino-driven Spartan Robokit.
* **Hardware Setup:** Assemble the physical components and wire the circuitry of the Spartan Robokit.
* **Testing:** Evaluate the physical robot using **5 distinct test points** (i.e., 5 different sets of values for the joint variables).
* **Application:** Program and execute a successful **pick-and-place task** relying exclusively on the Forward Kinematics method.
* **Submission:** Upload the finalized code into a designated folder within the GitHub repository created by the Project Engineer.

#### 3. Project Leader
* **Presentation Prep:** Prepare a strict **10-minute presentation** summarizing the preliminary project.
* **Presentation Content:** Ensure the presentation covers the following key areas:
  1. The labeled kinematic diagram, parametric table, and Homogeneous Transformation matrices of the Spartan Robokit.
  2. A review of the physical assembly and circuitry configuration.
  3. An explanation of the software integration between MATLAB and Arduino.
  4. Video/live demonstration of the physical forward kinematics motion.
  5. Mathematical verification proving the physical motion aligns with the calculated forward kinematics (based on lecture principles).
  6. Final conclusion.

---

### 📝 Standard D-H Transformation Matrix Reference
*Students: Utilize the standard Denavit-Hartenberg transformation matrix for your calculations:*

```text
[ cos(θi)  -sin(θi)cos(αi)   sin(θi)sin(αi)  ai*cos(θi) ]
[ sin(θi)   cos(θi)cos(αi)  -cos(θi)sin(αi)  ai*sin(θi) ]
[   0         sin(αi)          cos(αi)          di      ]
[   0            0                0              1      ]
