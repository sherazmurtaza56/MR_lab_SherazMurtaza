import rclpy
from rclpy.node import Node
import os

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')
        
        # TASK 3: Declare the parameter
        self.declare_parameter('student_name', 'Sheraz Murtaza')
        
        # Get the value
        name_val = self.get_parameter('student_name').get_parameter_value().string_value
        
        # Print the required outputs
        self.get_logger().info(f'Student Name: {name_val}')
        self.get_logger().info('Welcome to Mobile Robotics Lab')

        # TASK 2: Counter logic
        count_file = os.path.expanduser('~/count.txt')
        count = 1
        if os.path.exists(count_file):
            with open(count_file, 'r') as f:
                count = int(f.read()) + 1
        with open(count_file, 'w') as f:
            f.write(str(count))
            
        self.get_logger().info(f'Run count: {count}')

def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
