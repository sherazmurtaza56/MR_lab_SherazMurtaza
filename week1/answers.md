# Week 1 Post-Lab Answers

### 1. Definitions
* [cite_start]**Node:** A process that performs a specific computation or task within the ROS 2 network, such as a sensor driver or a controller[cite: 107, 135].
* [cite_start]**Topic:** A named communication channel used by nodes to exchange data through a publisher/subscriber model[cite: 107].
* [cite_start]**Package:** A container or organizational unit for ROS 2 code, containing everything needed to build and run a specific piece of software[cite: 111].
* [cite_start]**Workspace:** A dedicated directory where one or more ROS 2 packages are developed, built, and installed[cite: 111, 148].

### 2. Sourcing
[cite_start]Sourcing is required because it sets up the necessary environment variables in your terminal so that Ubuntu can locate ROS 2 commands and your specific workspace packages[cite: 140, 153]. [cite_start]If you do not source a workspace, you will receive errors like "command not found" when trying to use `ros2 run` or `colcon`[cite: 242, 244].

### 3. Colcon Build
[cite_start]The purpose of `colcon build` is to compile your source code into a runnable format and install it into your workspace[cite: 152, 258]. [cite_start]It generates four specific folders: `build/` (intermediate files), `install/` (executables), `log/` (build logs), and `src/` (which contains your code)[cite: 161, 162, 163, 258].

### 4. Entry Points in setup.py
[cite_start]The `entry_points` console script acts as a map that tells ROS 2 which command-line name (like `simple_node`) corresponds to a specific Python function (like `main`) in your code[cite: 190, 217, 259]. [cite_start]This allows you to run your Python script as an executable using the `ros2 run` command[cite: 128, 217].

### 5. Communication Diagram
Below is an ASCII diagram representing a simple Topic communication:

```text
    +------------------+                   +-------------------+
    |      Node A      |   /cmd_vel Topic  |      Node B       |
    |   (Publisher)    |------------------>|   (Subscriber)    |
    | (Sends Message)  |                   | (Receives Message)|
    +------------------+                   +-------------------+
