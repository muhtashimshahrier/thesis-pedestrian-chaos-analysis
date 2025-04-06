# bbox_conversion/polygon_to_bbox.py

import os
from PIL import Image
import argparse

def convert_polygon_to_bbox(components):
    xs = components[0::2]
    ys = components[1::2]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)
    x_center = (x_min + x_max) / 2
    y_center = (y_min + y_max) / 2
    width = x_max - x_min
    height = y_max - y_min
    return [x_center, y_center, width, height]

def is_polygon(components):
    return len(components) > 4

def convert_and_save_annotations(input_dir, output_dir, image_dir):
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if not filename.endswith(".txt"):
            continue

        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        image_path = os.path.join(image_dir, filename.replace('.txt', '.jpg'))

        try:
            with Image.open(image_path) as img:
                img_width, img_height = img.size
        except FileNotFoundError:
            print(f"Image not found: {filename}, skipping...")
            continue

        with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
            for line in infile:
                components = line.strip().split()
                class_id = components[0]
                coords = list(map(float, components[1:]))

                if is_polygon(coords):
                    bbox = convert_polygon_to_bbox(coords)
                else:
                    bbox = coords

                bbox_line = f"{class_id} " + " ".join(map(str, bbox)) + "\n"
                outfile.write(bbox_line)

    print(f"Converted annotations saved to: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert polygon annotations to bounding boxes.")
    parser.add_argument("--input_dir", type=str, required=True, help="Directory with input label .txt files")
    parser.add_argument("--output_dir", type=str, required=True, help="Directory to save converted labels")
    parser.add_argument("--image_dir", type=str, required=True, help="Directory containing corresponding images")

    args = parser.parse_args()
    convert_and_save_annotations(args.input_dir, args.output_dir, args.image_dir)
