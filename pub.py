#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String, Int32 
global count 
     
class RobotPublisher(Node): 
    def __init__(self):
        super().__init__("robot_Publisher") 
        self.count_ = 0
        # self.Publisher_ = self.create_subscription(String, "robot_news", self.callback_robot_news, 10)
        self.publisher_ = self.create_publisher(String, "robot_number", 10)
        self.timer_ = self.create_timer(1, self.send_number)
    #     self.get_logger().info("robot Publisher Node Started")
        
    # def callback_robot_news(self, msg):
    #     self.get_logger().info(msg.data)
            
    def send_number(self):
        number = String()
        number.data = '%d' %self.count_
        self.count_ +=1
        self.publisher_.publish(number)
        
def main(args=None):
    rclpy.init(args=args)
    node = RobotPublisher() 
    rclpy.spin(node)
    rclpy.shutdown()
     
     
if __name__ == "__main__":
    main()