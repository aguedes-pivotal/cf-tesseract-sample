from flask import Flask, jsonify, json
from socket import gethostname
from os import getenv
from PIL import Image
import pytesseract

app = Flask(__name__)


@app.route("/")
def hello():
    im = Image.open("sample1.jpg")
    text = pytesseract.image_to_string(im, lang = 'eng')

    return text, 200

port = int(getenv("PORT"))
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port, threaded=True)
