#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String, Int32 
global count 
     
class RobotSubscriber(Node): 
    def __init__(self):
        super().__init__("robot_subscriber") 
        self.count_ = 0
        self.subscriber_ = self.create_subscription(String, "robot_number", self.recieve_number, 10)
        # self.publisher_ = self.create_publisher(Int32, "robot_number", 10)
        # self.timer_ = self.create_timer(1, self.recieve_number)
        # self.get_logger().info("robot_subscriber and publisher Node Started")
        
    # def callback_robot_news(self, msg):
        # self.get_logger().info(msg.data)
            
    def recieve_number(self,number):
         self.get_logger().info(number.data)

        
def main(args=None):
    rclpy.init(args=args)
    node = RobotSubscriber() 
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()