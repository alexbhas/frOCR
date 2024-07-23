# FR > EN OCR
![image](https://github.com/alexbhas/frOCR/assets/56275911/2f1d0f57-aab7-40b0-8cf1-13001ca1c5bc)

## Description
This project is a Flask application that extracts text from images and translates it from French to English using the DeepL API and Tesseract OCR.

It was made because as I am learning french, I wanted to play video games in french and having a tool I can easily paste screenshots to into to translate helps a lot.

The language is easily interchangable by changing the language that the DeepL api expects to translate to/from, and the language Tesseract expects to read.

## Installation

Have a .env setup with your API key as DEEPL_API_KEY

```bash
git clone https://github.com/alexbhas/frOCR
cd frOCR
pip install -r requirements.txt
