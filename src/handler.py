import json
from src.libs import translation

def translate(event, context):
    input_text = "hello"
    translated = translation.transrate(input_text)

    response = {
        "inlang": translated.src,
        "outlang": translated.dest,
        "intext": input_text,
        "outtext": translated.text,
    }

    return response

def detect(event, context):
    input_text = "こんにちは"
    detected = translation.detect(input_text)

    response = {
        "lang": detected.lang,
        "confidence": detected.confidence,
        "intext": input_text,
    }

    return response
