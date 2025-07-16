from flask import Flask, request, render_template, jsonify
from transformers import CLIPProcessor, CLIPModel
import torch
import json
import numpy as np

app = Flask(__name__)

# Load CLIP model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load image data
with open("image_data.json") as f:
    image_data = json.load(f)

def search_images(query):
    inputs = processor(text=[query], return_tensors="pt", padding=True)
    text_embedding = model.get_text_features(**inputs)[0].detach().numpy()

    results = []
    for item in image_data:
        image_embedding = np.array(item['embedding'])
        similarity = np.dot(text_embedding, image_embedding) / (
            np.linalg.norm(text_embedding) * np.linalg.norm(image_embedding)
        )
        results.append((similarity, item))

    results.sort(reverse=True, key=lambda x: x[0])
    return [item for _, item in results[:10]]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    results = search_images(query)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
