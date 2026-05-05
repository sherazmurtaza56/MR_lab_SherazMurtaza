
## 🚀 About Me
```python?code_reference&code_event_index=1
# Define the content for the README.md file
readme_content = """# Custom Mobile Robot URDF Description

This repository contains the ROS 2 package for a custom differential drive mobile robot description using URDF. This project was developed as part of **Mobile Robotics Lab 8**.

## Project Overview
The goal of this project is to design and visualize a custom mobile robot in ROS 2. The robot features a box-shaped chassis and a cylindrical camera sensor. The model is built using the Unified Robot Description Format (URDF) and is visualized in RViz.

## Package Structure
```text
my_robot_description/
├── launch/          # Launch files for visualization
├── rviz/            # RViz configuration files
├── urdf/            # URDF model files
│   └── my_robot.urdf
├── CMakeLists.txt   # Build instructions
└── package.xml      # Package metadata
```

## Prerequisites
Ensure you have the following ROS 2 Humble packages installed:
```bash
sudo apt install ros-humble-urdf-tutorial
sudo apt install ros-humble-tf2-tools
```

## Installation & Setup
1. **Navigate to your workspace:**
   ```bash
   cd ~/ros2_ws/src
   ```
2. **Clone/Create the package** and place the files in `my_robot_description`.
3. **Build the workspace:**
   ```bash
   cd ~/ros2_ws
   colcon build --packages-select my_robot_description
   ```
4. **Source the setup file:**
   ```bash
   source install/setup.bash
   ```

## Usage
### Visualize in RViz
To launch the robot model and the joint state publisher GUI:
```bash
ros2 launch urdf_tutorial display.launch.py model:=$(ros2 pkg prefix my_robot_description)/share/my_robot_description/urdf/my_robot.urdf
```

### Verify Transform (TF) Tree
To inspect the coordinate frames and ensure correct parent-child relationships:
```bash
ros2 run tf2_tools view_frames
```

## Robot Features
- **Base Link:** 0.4m x 0.3m x 0.1m rectangular chassis.
- **Camera Sensor:** 0.05m radius, 0.05m length cylinder.
- **Joints:** Fixed joint connecting the camera to the base_link with a specific offset.

## Future Work
- Add **Inertial** and **Collision** tags for Gazebo simulation.
- Implement **Continuous Joints** for the differential drive wheels.
- Add a **LiDAR** sensor for SLAM and navigation tasks.
"""

