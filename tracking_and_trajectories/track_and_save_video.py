import cv2
import torch
from ultralytics import YOLO
from deep_sort import DeepSort
import argparse
import os

def run_tracking(video_path, model_path, output_path):
    # Load YOLOv8 model
    model = YOLO(model_path)
    deepsort = DeepSort()

    # Initialize video capture and output
    cap = cv2.VideoCapture(video_path)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)
        boxes = results[0].boxes.xywh.cpu().numpy()
        confs = results[0].boxes.conf.cpu().numpy()

        detections = []
        for i in range(len(boxes)):
            x, y, w, h = boxes[i]
            conf = confs[i]
            x1, y1, x2, y2 = x - w/2, y - h/2, x + w/2, y + h/2
            detections.append([x1, y1, x2, y2, conf])

        tracks = deepsort.update_tracks(detections, frame)

        for track in tracks:
            track_id = track[1]
            x, y, w, h = map(int, track[2])
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'ID {track_id}', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        out.write(frame)

    cap.release()
    out.release()
    print(f"Tracked video saved to: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Track and save video with YOLOv8 + DeepSORT.")
    parser.add_argument("--video", required=True, help="Path to input video")
    parser.add_argument("--model", required=True, help="Path to YOLOv8 model (.pt)")
    parser.add_argument("--output", default="tracked_output.mp4", help="Path to save output video")
    args = parser.parse_args()

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    run_tracking(args.video, args.model, args.output)
