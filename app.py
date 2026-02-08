from flask import Flask, send_file
import random
import string
import io
import os
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/')
def home():
    new_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    
    # Vercel par codes.txt temporary hoga, lekin testing ke liye theek hai
    with open("/tmp/codes.txt", "a") as f:
        f.write(new_code + "\n")
    
    try:
        # File dhoondne ka sahi tareeqa
        img_path = os.path.join(os.path.dirname(__file__), "random-code-image.png")
        font_path = os.path.join(os.path.dirname(__file__), "arial.ttf")

        img = Image.open(img_path).convert("RGB")
        draw = ImageDraw.Draw(img)
        
        if os.path.exists(font_path):
            font = ImageFont.truetype(font_path, 100)
        else:
            font = ImageFont.load_default()

        draw.text((380, 640), new_code, fill="white", font=font, stroke_width=2)
        
        img_io = io.BytesIO()
        img.save(img_io, 'JPEG', quality=100)
        img_io.seek(0)
        return send_file(img_io, mimetype='image/jpeg')
    except Exception as e:
        return f"Ibrahim, Error: {str(e)}"

# Vercel needs this
application = app
