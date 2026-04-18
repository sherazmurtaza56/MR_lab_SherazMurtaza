import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math

class TurtleFollower(Node):
    def __init__(self):
        super().__init__('turtle_follower')
        
        # Subscriber to get the Leader's position (Turtle 1)
        self.subscription_leader = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.leader_pose_callback,
            10)
            
        # Subscriber to get the Follower's position (Turtle 2)
        self.subscription_follower = self.create_subscription(
            Pose,
            '/turtle2/pose',
            self.follower_pose_callback,
            10)
            
        # Publisher to send velocity commands to the Follower (Turtle 2)
        self.publisher_follower = self.create_publisher(
            Twist,
            '/turtle2/cmd_vel',
            10)
            
        self.leader_pose = None
        self.follower_pose = None

    def leader_pose_callback(self, msg):
        self.leader_pose = msg
        self.move_follower()

    def follower_pose_callback(self, msg):
        self.follower_pose = msg

    def move_follower(self):
        # Wait until we have positions for both turtles
        if self.leader_pose is None or self.follower_pose is None:
            return

        msg = Twist()
        
        # Calculate distance between turtles
        dist = math.sqrt(
            (self.leader_pose.x - self.follower_pose.x)**2 + 
            (self.leader_pose.y - self.follower_pose.y)**2
        )
        
        # Calculate the angle towards the leader
        angle_to_leader = math.atan2(
            self.leader_pose.y - self.follower_pose.y,
            self.leader_pose.x - self.follower_pose.x
        )

        # Logic: If distance is more than 1 unit, move toward leader
        if dist > 1.0:
            # Linear velocity (speed) proportional to distance
            msg.linear.x = 1.5 * dist
            
            # Angular velocity (turning) to face the leader
            # We subtract current orientation (theta) from target angle
            angle_error = angle_to_leader - self.follower_pose.theta
            
            # Keep the angle error within -pi to pi
            if angle_error > math.pi:
                angle_error -= 2 * math.pi
            elif angle_error < -math.pi:
                angle_error += 2 * math.pi
                
            msg.angular.z = 4.0 * angle_error
        else:
            # Stop if close enough
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher_follower.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleFollower()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
