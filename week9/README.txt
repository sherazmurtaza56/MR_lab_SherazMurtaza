STUDENT NAME: Muhammad Sheraz Murtaza
ROLL NUMBER: 2022-MC-56
SECTION: B (EVEN)

PROJECT: ROS 2 Autonomous Recovery System (Marker-Based)

RECOVERY LOGIC EXPLANATION:
The system uses a Landmark-based approach. When the robot is "lost" (RViz and Gazebo coordinates mismatch), 
the 'marker_recovery' node waits for a specific ArUco marker detection. Once detected, it:
1. Overrides the failed AMCL pose with the Marker's absolute coordinates.
2. Triggers a Nav2 service to clear costmaps, removing "phantom" obstacles.
3. Resumes the path to the original goal autonomously.

RUN INSTRUCTIONS:
1. Launch Simulation: 
   ros2 launch turtlebot3_gazebo turtlebot3_house.launch.py
2. Launch Nav2 with Map: 
   ros2 launch turtlebot3_navigation2 navigation2.launch.py use_sim_time:=True map:=/path/to/your/map.yaml
3. Run Recovery Node: 
   source install/setup.bash
   ros2 run evaluation_package marker_recovery
4. Simulate Scan:
   ros2 topic pub /aruco_marker_publisher/markers aruco_msgs/MarkerArray "{markers: [{id: 1}]}" --once
