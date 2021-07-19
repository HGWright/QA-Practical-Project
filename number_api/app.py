from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_number', methods = ['GET'])
def get_number():
    ran_num = random.randint(15,21)
    return jsonify({"num": ran_num})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)