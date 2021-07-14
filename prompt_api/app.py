from flask import Flask, request, jsonify
import random

app = Flask(__name__)

@app.route('/get_prompt', methods = ['POST'])
def get_prompt():
    word_and_num = request.get_json()
    if len(word_and_num["word"]) <= 3 or word_and_num["num"] >= 10:
        prompt = random.choice(['while standing on one leg', 'while patting your head', 'while rubbing your belly'])
    else:
        prompt = 'with no additional challenge'
    return jsonify({"prompt": prompt})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)