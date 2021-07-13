from flask import Flask, request
from random import random.randint

@app.route('get_number', methods = ['GET'])
def get_number():
    ran_num = random.randint(0,21)
    return jasonify({"data": ran_num})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)