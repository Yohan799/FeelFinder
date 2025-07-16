import os
import requests

# 🔑 Replace with your actual Pexels API key
PEXELS_API_KEY = "uGxDZrRJo9e5DrYT7ijSXZUX0sBtb2Cr48AB7BHJJKbeQGFaeC9P5WUE"
headers = {"Authorization": PEXELS_API_KEY}

# Save location
base_path = r"D:\py files\files"
output_dir = os.path.join(base_path, "static", "images")
os.makedirs(output_dir, exist_ok=True)

queries = {
    "Joy": [
        "kids playing sparkler", "birthday cake fun", "festival dance",
        "smiling family", "joyful balloon"
    ],
    "Sadness": [
        "rainy window sad person", "lonely bench", "crying child",
        "deserted city street", "wilted flower"
    ],
    "Calm": [
        "sunrise beach", "forest path morning", "meditation scene",
        "calm lake reflection", "lavender field"
    ],
    "Anger": [
        "burning fire", "fists raised protest", "stormy sky", "broken glass"
    ],
    "Fear": [
        "dark forest", "lightning strike", "abandoned house", "shadowy alley"
    ],
    "Love": [
        "romantic candlelight dinner", "holding hands sunset",
        "couple kissing shadow", "heart rock beach"
    ],
    "Excitement": [
        "fireworks night", "rollercoaster scream", "cheering crowd"
    ],
    "Hope": [
        "sunrise hands reaching", "light ray through clouds"
    ]
}

def download_image(query, filename):
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=1"
    response = requests.get(url, headers=headers)
    data = response.json()
    photos = data.get("photos")
    if photos:
        image_url = photos[0]["src"]["large"]
        img_data = requests.get(image_url).content
        with open(os.path.join(output_dir, filename), 'wb') as f:
            f.write(img_data)
        print(f"✅ Downloaded: {filename}")
    else:
        print(f"❌ No result for: {query}")

# Start downloading
for category, search_terms in queries.items():
    for term in search_terms:
        filename = f"{term.replace(' ', '_').lower()}.jpg"
        download_image(term, filename)

print("\n🎉 All images downloaded to:", output_dir)
