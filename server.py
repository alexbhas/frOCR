from flask import Flask, request, render_template, jsonify, send_from_directory
import pytesseract
from PIL import Image
import os
import io
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    # Serve the HTML page
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    data = request.form['image']
    # Decode the image from base64
    img_data = base64.b64decode(data.split(',')[1])
    image = Image.open(io.BytesIO(img_data))
    # Use pytesseract to do OCR
    text = pytesseract.image_to_string(image, lang='fra')  # assuming French text
    # Translate text using DeepL
    translated_text = translate_text(text)
    return jsonify(original_text=text, translated_text=translated_text)

def translate_text(text):
    print("TEXT: ", text);
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        'auth_key': os.getenv('DEEPL_API_KEY'),
        'text': text,
        'target_lang': 'EN'
    }
    response = requests.post(url, data=params)
    result = response.json()
    print("API RESULT: ", result)
    return result['translations'][0]['text']

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    app.run(debug=True, port=5173)
