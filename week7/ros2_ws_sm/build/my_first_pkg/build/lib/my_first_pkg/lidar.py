import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np

class LidarNavigator(Node):

    def __init__(self):
        super().__init__('lidar_navigator')
        
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # TODO: Define thresholds
        self.front_threshold = 0.5  # Meters
        self.side_threshold = 0.5   # Meters

    def scan_callback(self, msg):
        # Convert ranges to a numpy array for easier processing [cite: 78]
        ranges = np.array(msg.ranges)
        
        # -----------------------------
        # TODO 1: Clean data (remove inf/nan)
        # -----------------------------
        # Replace inf with a large value and NaN with 0
        ranges[np.isinf(ranges)] = 3.5 
        ranges[np.isnan(ranges)] = 0.0
        
        # -----------------------------
        # TODO 2: Define regions
        # -----------------------------
        # For TurtleBot3, 0 is front, 90 is left, 270 is right
        # We take slices of the array for each region
        front_region = np.concatenate((ranges[0:15], ranges[345:359]))
        left_region = ranges[45:135]
        right_region = ranges[225:315]
        
        # Compute minimum distance in each region
        front_dist = np.min(front_region)
        left_dist = np.min(left_region)
        right_dist = np.min(right_region)
        
        twist = Twist()
        
        # -----------------------------
        # TODO 3: Obstacle logic
        # -----------------------------
        if front_dist < self.front_threshold:
            # Obstacle in front: Stop linear motion and turn
            twist.linear.x = 0.0
            
            # -------------------------
            # TODO 4: Turn direction
            # -------------------------
            if left_dist > right_dist:
                # Left is clearer, turn left (positive angular z)
                twist.angular.z = 0.5 
            else:
                # Right is clearer or equal, turn right (negative angular z)
                twist.angular.z = -0.5
        else:
            # -------------------------
            # TODO 5: Forward motion
            # -------------------------
            # Path is clear, move forward at suggested speed
            twist.linear.x = 0.15 
            twist.angular.z = 0.0
            
        # Publish the command to /cmd_vel
        self.publisher.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = LidarNavigator()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()