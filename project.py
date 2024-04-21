import cv2
from ultralytics import YOLO

# Load YOLO model
src = 'best2.pt'
model = YOLO(src)

# Open video file
video_path = 'fruits.mp4'
cap = cv2.VideoCapture(video_path)

# Define a function to process video frames and display them with OpenCV
def process_video():
    so_luong_tao = 0
    so_luong_chuoi = 0
    so_luong_nho = 0
    so_luong_cam = 0
    so_luong_khom = 0
    so_luong_duahau= 0
    frame_count = 0

    while True:
        # Read frame from the video
        ret, frame = cap.read()
        if not ret:
            break
        
        # Process the frame with YOLO
        results = model(frame)
        frame_count += 1

        # Draw bounding boxes and labels on the frame
        for result in results:
            for box in result.boxes.data:
                xmin, ymin, xmax, ymax = map(int, box[:4])
                # Increment fruit counts based on class
                if box[5] == 0:
                    so_luong_tao += 1
                    label = f"Táo: {box[4] * 100:.2f}%"
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (72, 72, 208), 2)
                    cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (72, 72, 208), 2)
                elif box[5] == 1:
                    so_luong_chuoi += 1
                    label = f"Chuối: {box[4] * 100:.2f}%"
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (74, 201, 255), 2)
                    cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (74, 201, 255), 2)
                elif box[5] == 2:
                    so_luong_nho += 1
                    label = f"Nho: {box[4] * 100:.2f}%"
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (156, 70, 134), 2)
                    cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (156, 70, 134), 2)
                elif box[5] == 3:
                    so_luong_cam += 1
                    label = f"Cam: {box[4] * 100:.2f}%"
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 152, 255), 2)
                    cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 152, 255), 2)
                elif box[5] == 4:
                    label = f"Khớm: {box[4] * 100:.2f}%"
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (67, 152, 255), 2)
                    cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (67, 152, 255), 2)
                    so_luong_khom += 1
                elif box[5] == 5:
                    so_luong_duahau += 1
                    label = f"Dưa Hấu: {box[4] * 100:.2f}%"
                    cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (85, 38, 175), 2)
                    cv2.putText(frame, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (85, 38, 175), 2)
                    so_luong_khom += 1

        # Display the frame with bounding boxes and labels
        cv2.imshow('Frame', frame)

        # Check for 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    # Print fruit counts
    print("Số lượng frame:", frame_count)
    print("-----------------------------------------------------")
    print("Tổng số lượng táo được phát hiện:", so_luong_tao)
    print("Tổng số lượng chuối được phát hiện:", so_luong_chuoi)
    print("Tổng số lượng nho được phát hiện:", so_luong_nho)
    print("Tổng số lượng cam được phát hiện:", so_luong_cam)
    print("Tổng số lượng khom được phát hiện:", so_luong_khom)
    print("Tổng số lượng dưa hấu được phát hiện:", so_luong_duahau)
    print("-----------------------------------------------------")
    print("Số lượng táo trung bình:", round(so_luong_tao / frame_count,2))
    print("Số lượng chuối trung bình:", round(so_luong_chuoi / frame_count,2))
    print("Số lượng nho trung bình:", round(so_luong_nho / frame_count, 2))
    print("Số lượng cam trung bình:", round(so_luong_cam / frame_count, 2))
    print("Số lượng khom trung bình:", round(so_luong_khom / frame_count, 2))
    print("Số lượng dưa hấu trung bình:", round(so_luong_duahau / frame_count,2))

# Call the function to start processing the video
process_video()
