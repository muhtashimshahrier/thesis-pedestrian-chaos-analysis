# Image Extraction from Video

This script extracts frames from a video at fixed time intervals using OpenCV. It was used during dataset preparation as part of my undergraduate thesis.

---

## Features

- Captures frames at regular intervals (e.g., every 5 seconds)
- Fully configurable through command-line arguments
- Automatically creates the output directory
- Uses relative paths for easy GitHub integration

---

### Command-Line Example

```bash
python extract_images.py \
  --video ../data/videos/10.mp4 \
  --output ../data/extracted_frames/10/ \
  --interval 5
