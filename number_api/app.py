from flask import Flask, request
from random import random.randint

@app.route('get_number', methods = ['GET'])
def get_number():
    return random.randint(0,21)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)