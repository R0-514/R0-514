#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
import time
     
     
class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.pose_ = None
        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        # self.pose_subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.callback_turtle_pose, 10)
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
        #self.servce_ = self.create_service(MoveLocation, "move_location", self.callback_get_distance)

    def control_loop(self):
        msg = Twist()
        msg.linear.x = 5.0
        msg.angular.z = 2*math.pi
        self.cmd_vel_publisher_.publish(msg)
   
def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()
    
       
if __name__ == "__main__":
	main()