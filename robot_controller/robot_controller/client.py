import rclpy
from rclpy.node import Node
from ros_interface.srv import SetMode


class ModeClient(Node):

    def __init__(self):
        super().__init__('mode_client')

        self.client = self.create_client(
            SetMode,
            'set_mode'
        )

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'waiting for service...'
            )

    def send_request(self, mode):

        request = SetMode.Request()
        request.mode = mode

        future = self.client.call_async(request)

        rclpy.spin_until_future_complete(
            self,
            future
        )

        return future.result()


def main(args=None):
    rclpy.init(args=args)

    node = ModeClient()

    response = node.send_request('AUTO')

    print(response.success)
    print(response.message)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
