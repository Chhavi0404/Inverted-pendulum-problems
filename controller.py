#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from custom_msgs.msg import States , TorqueInput


class MyNode(Node):
    def __init__(self):

        self.torque_provided = 5.0

        super().__init__("controller")
        self.state_subscriber = self.create_subscription(States,"/state_feedback",self.state_callback,10)
        self.torque_publisher = self.create_publisher(TorqueInput,"/torque_input" , 10) 
    

        self.get_logger().info(str(f"Torque provided is {self.torque_provided}"))

    def state_callback(self, msg):
        cmd = TorqueInput()
        cmd.torque_value = self.torque_provided
        self.torque_publisher.publish(cmd)

def main(args = None):
    rclpy.init(args = args)
    node = MyNode( )
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()