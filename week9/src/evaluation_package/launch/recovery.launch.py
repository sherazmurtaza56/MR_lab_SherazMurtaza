from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tag_recovery',
            executable='recovery_node',
            name='recovery_node',
            output='screen',
            emulate_tty=True,
            parameters=[{
                'use_sim_time': True,
                'tag_x': 7.425,     # <--- EDIT THIS
                'tag_y': 4.4343,     # <--- EDIT THIS
                'robot_yaw': 0.0,   # <--- EDIT THIS
                'tag_size': 0.27    # <--- EDIT THIS
            }]
        )
    ])
