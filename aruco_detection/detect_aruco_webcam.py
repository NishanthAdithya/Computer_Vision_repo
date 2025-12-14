import cv2
from aruco_utils import get_aruco_detector

def main():
    aruco_dict, parameters = get_aruco_detector()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("ERROR: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Frame not received.")
            break

        # THE FIX: explicitly pass parameters=parameters
        corners, ids, _ = cv2.aruco.detectMarkers(
            frame,
            aruco_dict,
            parameters=parameters
        )

        if ids is not None:
            for marker_id, corner in zip(ids, corners):
                cv2.polylines(frame, [corner.astype(int)], True, (0,255,0), 2)
                cv2.putText(frame, f"ID: {int(marker_id)}",
                    (int(corner[0][0][0]), int(corner[0][0][1]) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
            print("Detected IDs:", ids.flatten())

        cv2.imshow("Webcam ArUco Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
