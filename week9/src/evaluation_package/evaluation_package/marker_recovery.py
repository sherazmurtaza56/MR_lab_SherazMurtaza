import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseWithCovarianceStamped
from cv_bridge import CvBridge
import cv2
import math

class MarkerRecoveryNode(Node):
    def __init__(self):
        super().__init__('marker_recovery_node')
        self.subscription = self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)
        # Using /amcl/initialpose ensures Nav2 listens to the update
        self.pose_publisher = self.create_publisher(PoseWithCovarianceStamped, '/amcl/initialpose', 10)
        self.br = CvBridge()
        self.is_armed = True  
        
        # Exact values from your latest Gazebo screenshot
        self.TAG_MAP_X = -0.140637 
        self.TAG_MAP_Y = 4.633481
        
        self.get_logger().info('Recovery System Online. Drive to the AprilTag to sync...')

    def image_callback(self, msg):
        try:
            cv_image = self.br.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception:
            return
        gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_APRILTAG_36h11)
        parameters = cv2.aruco.DetectorParameters()
        detector = cv2.aruco.ArucoDetector(dictionary, parameters)
        corners, ids, rejected = detector.detectMarkers(gray)

        if ids is not None and self.is_armed:
            self.get_logger().info('AprilTag DETECTED! Aligning RViz with Gazebo...')
            recovery_pose = PoseWithCovarianceStamped()
            recovery_pose.header.frame_id = 'map'
            recovery_pose.header.stamp = self.get_clock().now().to_msg()
            
            # Setting the robot position to the known tag location
            recovery_pose.pose.pose.position.x = self.TAG_MAP_X
            recovery_pose.pose.pose.position.y = self.TAG_MAP_Y
            
            # Setting low covariance to force an immediate snap in RViz
            recovery_pose.pose.covariance[0] = 0.01
            recovery_pose.pose.covariance[7] = 0.01
            recovery_pose.pose.covariance[35] = 0.01
            
            self.pose_publisher.publish(recovery_pose)
            self.is_armed = False # Prevent jumping after sync
            self.get_logger().info('Sync Complete. RViz is now aligned.')

def main(args=None):
    rclpy.init(args=args)
    node = MarkerRecoveryNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
