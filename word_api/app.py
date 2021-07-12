from flask import Flask, request
from random import random.choice

app = Flask(__name__)

@app.route('/get_word', methods = ['GET'])
def get_word():
    return random.choice(['Happy', 'Donkey', 'Swing'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)