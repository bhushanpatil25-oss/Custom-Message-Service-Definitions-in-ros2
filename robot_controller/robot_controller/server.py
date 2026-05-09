import rclpy
from rclpy.node import Node
from ros_interface.srv import SetMode


class ModeServer(Node):

    def __init__(self):
        super().__init__('mode_server')

        self.service = self.create_service(
            SetMode,
            'set_mode',
            self.callback
        )

    def callback(self, request, response):

        self.get_logger().info(
            f"Requested mode: {request.mode}"
        )

        if request.mode in ['AUTO', 'MANUAL']:
            response.success = True
            response.message = "Mode changed"
        else:
            response.success = False
            response.message = "Invalid mode"

        return response


def main(args=None):
    rclpy.init(args=args)

    node = ModeServer()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()
