from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_word', methods = ['GET'])
def get_word():
    ran_word = random.choice(['Happy', 'Donkey', 'Swing', 'Bee', 'Party'])
    return jsonify({"word": ran_word})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)