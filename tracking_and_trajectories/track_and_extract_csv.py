import cv2
import pandas as pd
from ultralytics import YOLO
from deep_sort import DeepSort
import argparse
import os

def track_and_extract(video_path, model_path, class_id, output_csv):
    model = YOLO(model_path)
    deepsort = DeepSort()
    cap = cv2.VideoCapture(video_path)

    trajectory_data = []
    frame_idx = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_idx += 1
        results = model(frame)

        boxes = results[0].boxes.xywh.cpu().numpy()
        confs = results[0].boxes.conf.cpu().numpy()
        class_ids = results[0].boxes.cls.cpu().numpy()

        filtered = [
            (boxes[i], confs[i])
            for i in range(len(class_ids))
            if class_ids[i] == class_id
        ]

        detections = []
        for box, conf in filtered:
            x, y, w, h = box
            x1, y1, x2, y2 = x - w/2, y - h/2, x + w/2, y + h/2
            detections.append([x1, y1, x2, y2, conf])

        tracks = deepsort.update_tracks(detections, frame)

        for track in tracks:
            track_id = track[1]
            x, y, w, h = track[2]
            trajectory_data.append([frame_idx, track_id, x, y, w, h])

    cap.release()
    df = pd.DataFrame(trajectory_data, columns=["Frame", "ID", "X", "Y", "Width", "Height"])
    os.makedirs(os.path.dirname(output_csv), exist_ok=True)
    df.to_csv(output_csv, index=False)
    print(f"Trajectory CSV saved to: {output_csv}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Track and extract trajectory CSV using YOLOv8 + DeepSORT.")
    parser.add_argument("--video", required=True, help="Path to input video")
    parser.add_argument("--model", required=True, help="Path to YOLOv8 model (.pt)")
    parser.add_argument("--class-id", type=int, default=11, help="Target class ID to track")
    parser.add_argument("--output", default="trajectory_output.csv", help="Output CSV file path")
    args = parser.parse_args()

    track_and_extract(args.video, args.model, args.class_id, args.output)
