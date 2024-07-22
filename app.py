from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.get_json()
    if 'value' not in data or not isinstance(data['value'], int):
        return jsonify({'error': 'Invalid input'}), 400
    
    value = data['value']
    if value > 100:
        result = 'high'
    else:
        result = 'low'
    
    return jsonify({'value': result})

if __name__ == '__main__':
    app.run(debug=True)
