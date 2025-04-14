from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return jsonify({"message": "To jest moja strona!"})

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Nieznajomy')
    return jsonify({"message": f"Witaj, {name}!"})

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        
        if num1 + num2 > 5.8:
            return jsonify({"prediction": 1})
        else:
            return jsonify({"prediction": 0})
    except (TypeError, ValueError):
        return jsonify({"error": "Proszę podać dwie liczby jako parametry 'num1' i 'num2'"}), 400

if __name__ == '__main__':
    app.run(port=5000)
