import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped
import sys # Added for command line arguments

class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')
        self._client = ActionClient(self, FollowWaypoints, 'follow_waypoints')

    def send_waypoints(self, waypoints):
        self.get_logger().info('Waiting for FollowWaypoints action server...')
        self._client.wait_for_server()

        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = waypoints

        self.get_logger().info(f'Sending {len(waypoints)} waypoints...')
        
        send_goal_future = self._client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)
        
        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected by server!')
            return

        self.get_logger().info('Goal accepted. Navigating...')
        
        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)
        self.get_logger().info('All waypoints reached!')

def make_pose(x, y, yaw_w):
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = rclpy.clock.Clock().now().to_msg()
    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = 0.0
    pose.pose.orientation.z = 0.0 # Standard z for 2D orientation
    pose.pose.orientation.w = yaw_w
    return pose

def main(args=None):
    rclpy.init(args=args)
    
    # 1. Capture arguments from the command line
    # sys.argv[0] is the script name, so we start from sys.argv[1:]
    raw_args = sys.argv[1:]

    # 2. Check if we have multiples of 3 (x, y, w)
    if len(raw_args) < 3 or len(raw_args) % 3 != 0:
        print("Usage: python3 waypoint_navigator.py x1 y1 w1 x2 y2 w2 ...")
        print("Please provide coordinates in groups of three.")
        return

    # 3. Parse arguments into the waypoints list
    waypoints = []
    try:
        for i in range(0, len(raw_args), 3):
            x = float(raw_args[i])
            y = float(raw_args[i+1])
            w = float(raw_args[i+2])
            waypoints.append(make_pose(x, y, w))
    except ValueError:
        print("Error: All arguments must be numbers.")
        return

    navigator = WaypointNavigator()
    navigator.send_waypoints(waypoints)
    
    navigator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
