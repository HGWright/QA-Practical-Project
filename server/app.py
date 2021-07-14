from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    word = requests.get('http://word_api:5003/get_word')
    word_dict = word.json()
    number = requests.get('http://number_api:5001/get_number')
    number_dict = number.json()
    prompt = requests.post('http://prompt_api:5002/get_prompt', json = {"word": word_dict["word"], "num": number_dict["num"]})
    prompt_dict = prompt.json()
    return render_template('index.html', word = word_dict["word"], number = number_dict["num"], prompt = prompt_dict["prompt"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)