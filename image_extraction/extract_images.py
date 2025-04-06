# image_extraction/extract_images.py

import cv2
import os
import argparse

def extract_frames(video_path, output_dir, interval_sec):
    os.makedirs(output_dir, exist_ok=True)

    vidcap = cv2.VideoCapture(video_path)
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * interval_sec)

    count = 0
    saved_count = 0

    while vidcap.isOpened():
        ret, frame = vidcap.read()
        if not ret:
            break

        if count % frame_interval == 0:
            frame_number = int(count // fps)
            filename = os.path.join(output_dir, f"{frame_number}.jpg")
            cv2.imwrite(filename, frame)
            saved_count += 1

        count += 1

    vidcap.release()
    cv2.destroyAllWindows()
    print(f"Extraction complete. {saved_count} frames saved to: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract frames from video every N seconds.")
    parser.add_argument("--video", type=str, required=True, help="Path to input video file")
    parser.add_argument("--output", type=str, required=True, help="Directory to save extracted frames")
    parser.add_argument("--interval", type=int, default=5, help="Interval (in seconds) between frames")

    args = parser.parse_args()
    extract_frames(args.video, args.output, args.interval)
