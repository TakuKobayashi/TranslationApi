# coding:utf-8

from flask import Flask, request

from src.libs import translation
import json

import os
from os.path import join, dirname

app = Flask(__name__)

@app.route("/transrate", methods=["GET", "POST"])
def transrate():
    input_text = request.get_data()
    print(input_text)
    translated = translation.transrate("hello")
    return json.dumps({
        "inlang": translated.src,
        "outlang": translated.dest,
        "intext": input_text,
        "outtext": translated.text,
    }, ensure_ascii=False)

@app.route("/detect", methods=["GET", "POST"])
def detect():
    input_text = "こんにちは"
    detected = translation.detect(input_text)
    return json.dumps({
        "lang": detected.lang,
        "confidence": detected.confidence,
        "intext": input_text,
    }, ensure_ascii=False)

if __name__ == "__main__":
    app.debug = True
    app.host = '0.0.0.0'
    app.threaded = True
    app.run()