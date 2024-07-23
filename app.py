# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello_world():
    num = int(request.json['num'])
    if num > 100:
        response = {'value': num, 'description': 'high'}
    else:
        response = {'value': num, 'description': 'low'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)