from googletrans import Translator

def transrate(input_text, src='en', dest='ja'):
    translator = Translator()
    return translator.translate(input_text, src=src, dest=dest)

def detect(input_text):
    translator = Translator()
    return translator.detect(input_text)