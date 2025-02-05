#!/usr/bin/python3
import json
from flask import Blueprint, request, Response
from app.utils import classify_number

main = Blueprint('main', __name__)

@main.route('/api/classify-number', methods=['GET'])
def classify():
    number = request.args.get('number')

    if not number or not number.lstrip('-').isdigit():
        return Response(
            json.dumps({"number": number, "error": True}),
            status=400,
            mimetype='application/json'
        )

    number = int(number)
    result = classify_number(number)
    response = Response(
        json.dumps(result, sort_keys=False),
        mimetype='application/json'
    )
    return response, 200