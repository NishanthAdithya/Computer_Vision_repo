import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

import cv2
from aruco_utils import get_aruco_detector

class ArucoDetectorNode(Node):

    def __init__(self):
        super().__init__('aruco_detector')
        self.bridge = CvBridge()
        self.detector = get_aruco_detector()

        self.subscription = self.create_subscription(
            Image,
            '/camera/color/image_raw',
            self.image_callback,
            10
        )

        self.get_logger().info("Aruco Detector Node Started (6x6_250)")

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        corners, ids, _ = self.detector.detectMarkers(frame)

        if ids is not None:
            for i, corner in zip(ids, corners):
                cv2.polylines(frame, [corner.astype(int)], True, (0,255,0), 2)
                cv2.putText(frame, f"ID: {int(i)}",
                            (int(corner[0][0][0]), int(corner[0][0][1]) - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

            print("Detected IDs:", ids.flatten())

        cv2.imshow("ROS2 ArUco Detection", frame)
        cv2.waitKey(1)


def main():
    rclpy.init()
    node = ArucoDetectorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
