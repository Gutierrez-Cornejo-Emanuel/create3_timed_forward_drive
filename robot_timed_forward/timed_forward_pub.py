import rclpy
import time
from rclpy.node import Node

from geometry_msgs.msg import Twist


class TimedForwardPublisher(Node):

    def __init__(self):
        super().__init__('timed_forward_publisher')
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.process_input()
    
    def process_input(self):
        while True:
            user_input = input("Enter integer here: ")
            if not str(user_input).isdigit():
                print("Not an intrger!")
                continue
            start_time = time.time()

            # Continue printing until n seconds have passed
            while time.time() - start_time < int(user_input):
                msg = Twist()
                msg.linear.x = 0.2
                self.publisher.publish(msg)
                print("publishing")
                time.sleep(0.1)




def main(args=None):
    rclpy.init(args=args)

    timed_forward_publisher = TimedForwardPublisher()

    rclpy.spin(timed_forward_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    timed_forward_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()