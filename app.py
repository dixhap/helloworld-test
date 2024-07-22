# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/compare', methods=['POST'])
def compare_number():
    num = int(request.json['number'])
    if num > 100:
        result = 'high'
    else:
        result = 'low'
    return jsonify({'number': num, 'result': result})

if __name__ == '__main__':
    app.run(debug=True)