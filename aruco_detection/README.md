# ArUco Marker Detector (6x6_250)

This project provides two detection modes:

1. **Webcam Detection** using OpenCV
2. **ROS2 Camera Topic Detection** using /camera/color/image_raw

Both detect **ArUco markers (DICT_6X6_250)** and print:
- Marker ID
- Bounding boxes
- Live visualization

---

## Folder Structure
aruco_detector/
│── detect_aruco_webcam.py
│── detect_aruco_ros2.py
│── aruco_utils.py
│── requirements.txt
└── README.md


---

## Install Requirements

pip install -r requirements.txt

For ROS2:

sudo apt install ros-humble-cv-bridge
---

## Run Webcam Version
python3 detect_aruco_webcam.py

Press **Q** to quit.

---

## Run ROS2 Version

Terminal 1:
ros2 run your_camera_driver

Terminal 2:
python3 detect_aruco_ros2.py


Shows live detection and prints IDs.

---

## Marker Dictionary
This project uses:

DICT_6X6_250

---

## Notes
- Webcam version uses `VideoCapture(0)`
- ROS2 version uses `/camera/color/image_raw`
- Both scripts share the same detection logic in `aruco_utils.py`
