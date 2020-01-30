import json
from src.libs import translation


def translate(event, context):
    input_params = parse_input_params(event)
    if input_params['input_text'] is not None:
        translated = translation.transrate(input_params['input_text'], src=input_params['input_src'],
                                           dest=input_params['input_dest'])
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "inlang": translated.src,
                "outlang": translated.dest,
                "intext": input_params['input_text'],
                "outtext": translated.text,
            }, ensure_ascii=False)
        }
    else:
        response = {
            "statusCode": 400,
            "body": 'sentence is none',
        }

    return response


def detect(event, context):
    input_params = parse_input_params(event)
    if input_params['input_text'] is not None:
        detected = translation.detect(input_params['input_text'])
        response = {
            "statusCode": 200,
            "body": json.dumps({
                "lang": detected.lang,
                "confidence": detected.confidence,
                "intext": input_params['input_text'],
            }, ensure_ascii=False)
        }
    else:
        response = {
            "statusCode": 400,
            "body": 'sentence is none',
        }

    return response


def parse_input_params(event):
    result = {
        'input_text': None,
        'input_src': 'en',
        'input_dest': 'ja',
    }
    query_params = event['queryStringParameters']
    body_parser = {}
    try:
        if event['body'] is not None:
            body_parser = json.loads(event['body'])
    except ValueError:
        pass

    if 'sentence' in query_params:
        result['input_text'] = query_params['sentence']
    elif 'sentence' in body_parser:
        result['input_text'] = body_parser['sentence']
    else:
        return result

    if 'src' in query_params:
        result['input_src'] = query_params['src']
    elif 'src' in body_parser:
        result['input_src'] = body_parser['src']
    else:
        detected = translation.detect(result['input_text'])
        result['input_src'] = detected.lang

    if 'dest' in query_params:
        result['input_dest'] = query_params['dest']
    elif 'dest' in body_parser:
        result['input_dest'] = body_parser['dest']
    return result
