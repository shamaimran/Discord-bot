import os
from flask import Flask, send_file
import random
import string
import io
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)
# Ibrahim, file ka naam wahi rakhein jo aapne upload ki hai
IMAGE_PATH = "random-code-image.png" 

@app.route('/')
def home():
    # 1. Unique code banana
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    # 2. Codes ko save karna bot ke liye
    with open("codes.txt", "a") as f:
        f.write(new_code + "\n")
    
    try:
        img = Image.open(IMAGE_PATH).convert("RGB")
        draw = ImageDraw.Draw(img)
        
        # 3. BADA FONT SETUP
        # Humne arial.ttf upload ki hai, usay use karenge
        font_size = 100 
        font = ImageFont.truetype("arial.ttf", font_size)

        # 4. Text Position (Ibrahim, ye coordinates perfect hain)
        # (380, 640) par code bilkul "Your Random Code:" ke niche aayega
        draw.text((380, 640), new_code, fill="white", font=font)
        
        img_io = io.BytesIO()
        img.save(img_io, 'JPEG', quality=100)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')
        
    except Exception as e:
        return f"Ibrahim, Error: {e}"

# Aakhri lines ko aise likhein
if __name__ == "__main__":
    app.run(debug=True)
else:
    # Vercel ke liye
    app = app