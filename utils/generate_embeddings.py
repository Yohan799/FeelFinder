import os
import json
from PIL import Image
import torch
import numpy as np
from transformers import CLIPProcessor, CLIPModel

# Define paths
base_path = r"D:\py files\files"
image_folder = os.path.join(base_path, "static", "images")
output_file = os.path.join(base_path, "image_data.json")

# Load CLIP model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

image_data = []

print(f"🖼 Processing images in: {image_folder}")
for filename in os.listdir(image_folder):
    if not filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue

    filepath = os.path.join(image_folder, filename)
    image = Image.open(filepath).convert("RGB")

    # Preprocess and get image features
    inputs = processor(images=image, return_tensors="pt")
    with torch.no_grad():
        embedding = model.get_image_features(**inputs)[0].numpy().tolist()

    # Save metadata + embedding
    image_data.append({
        "title": filename.replace("_", " ").replace(".jpg", "").title(),
        "url": f"/static/images/{filename}",
        "embedding": embedding
    })
    print(f"✅ Embedded: {filename}")

# Write to JSON
with open(output_file, "w") as f:
    json.dump(image_data, f, indent=2)

print(f"\n📁 Saved embeddings to: {output_file}")
