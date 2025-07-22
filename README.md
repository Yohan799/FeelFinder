
# 🎯 FeelFinder - Emotion-Based Image Search Engine

**FeelFinder** is a smart web application that allows users to search for images using natural language expressions of **emotion**, **mood**, or **sentiment**. It leverages the power of **computer vision** (via OpenAI's CLIP model) and **natural language processing** to retrieve images that best match the *feeling* behind the user's query.

---

## 🌟 Features

- 🔍 Search for images using mood/emotion-based text queries  
- 🧠 Powered by CLIP: Understands both language and vision  
- 🖼️ Returns the top-matching images from a curated dataset  
- 💻 Clean and responsive frontend with HTML/CSS/JavaScript  
- ⚙️ Lightweight backend using Python Flask  

---

## 🧠 How It Works

1. **Preprocess Images**  
   - Each image is embedded using the **CLIP** model (`image -> vector`).
   - The result is saved to `image_data.json`.

2. **Search by Text**  
   - The user's query (e.g., `"peaceful sunset"`) is also embedded (`text -> vector`).
   - The backend compares the text vector with each image vector using **cosine similarity**.

3. **Top Matches Displayed**  
   - The best-matching images are sent to the frontend.
   - The user sees relevant images that match their mood/sentiment.

---

## 📦 Folder Structure

```
project-root/
│
├── app.py                      # Flask backend
├── image_data.json             # Precomputed image embeddings
│
├── static/
│   ├── styles.css              # Frontend styling
│   └── images/                 # All image files
│
├── templates/
│   └── index.html              # Main frontend page
│
├── utils/
│   ├── download_images.py      # Download images by mood from Pexels
│   └── generate_embeddings.py  # Generate CLIP embeddings for images
│
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container setup
├── README.md                   # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/moodlens.git
cd moodlens
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download Images (Optional)

Update your Pexels API key in `utils/download_images.py`, then run:

```bash
python utils/download_images.py
```

### 4. Generate Embeddings

```bash
python utils/generate_embeddings.py
```

### 5. Run the App

```bash
python app.py
```

Open your browser at: [http://localhost:5000](http://localhost:5000)

---

## 💬 Example Search Queries

- `"joyful kids"`
- `"calm ocean scene"`
- `"angry protest"`
- `"hopeful sunrise"`
- `"romantic candlelight"`

---

## 📷 Preview

![Storyboard Demo](https://github.com/yohan799/FeelFinder/blob/main/demo1.png/)

## 🧰 Tech Stack

| Layer     | Technology         |
|-----------|--------------------|
| Frontend  | HTML, CSS, JavaScript |
| Backend   | Python Flask       |
| AI Model  | OpenAI CLIP (via 🤗 Transformers) |
| Data      | JSON / Static Images |
| Image API | Pexels (for dataset) |

---

## 📦 requirements.txt

```
flask
torch
transformers
pillow
numpy
requests
```

---

## 🐳 Dockerfile

```dockerfile
# Use Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

- [OpenAI CLIP](https://github.com/openai/CLIP)
- [HuggingFace Transformers](https://huggingface.co/)
- [Pexels Free Image API](https://www.pexels.com/api/)
