# Mobile Robotics Lab - Week 1
**Student Name:** Sheraz Murtaza  
**Course:** MCT-454L Mobile Robotics  
**Instructor:** Dr. Maria Akram  

## Lab Description
[cite_start]This lab focused on the fundamentals of Linux and ROS 2 Humble[cite: 2, 4]. [cite_start]The primary objectives were setting up a ROS 2 development workspace, creating a Python-based package named `my_first_pkg`, and developing a node (`simple_node`) that utilizes logging, file I/O for persistent data, and ROS 2 parameters[cite: 7, 8, 9, 252, 253].

## Commands Used
Throughout the lab, the following core commands were utilized for development and workspace management:

* [cite_start]`mkdir -p ~/ros2_ws_sm/src`: Created the workspace and source directory[cite: 150].
* [cite_start]`ros2 pkg create --build-type ament_python my_first_pkg`: Created the ROS 2 Python package[cite: 169].
* [cite_start]`colcon build`: Compiled the workspace packages[cite: 172].
* [cite_start]`source install/setup.bash`: Sourced the workspace to make packages available in the current terminal[cite: 173].
* [cite_start]`ros2 run my_first_pkg simple_node`: Executed the custom node[cite: 234].
* [cite_start]`ros2 run my_first_pkg simple_node --ros-args -p student_name:="Sheraz Murtaza"`: Ran the node while passing a ROS parameter[cite: 253].

## Problems Faced and Solutions
1. **Workspace Naming:** Initially, I encountered "No such file or directory" errors because my workspace was named `ros2_ws_sm` instead of the default `ros2_ws`. I resolved this by ensuring all paths in my commands matched my actual directory structure.
2. **Build Refreshing:** Changes to the Python script were not immediately appearing when running the node. [cite_start]I solved this by using `colcon build --symlink-install`, which allowed changes to take effect without a full rebuild[cite: 250].
3. **GitHub Authentication:** Pushing to GitHub required a Personal Access Token (PAT) rather than a standard password. I generated a PAT in GitHub settings to successfully authenticate the `git push`.

## Reflection
This lab was my first introduction to the Ubuntu environment and the ROS 2 framework. Moving from a GUI-based workflow to a terminal-centric one was challenging but rewarding. Learning how nodes communicate and how the workspace handles dependencies provided a strong foundation for future robotics tasks. Successfully implementing the persistent counter and ROS parameters showed me how versatile even a simple node can be. I am now more confident in managing packages and using Git for version control.
