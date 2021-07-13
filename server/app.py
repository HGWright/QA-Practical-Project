from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    word = requests.get('http://word_api:5000/get_word')
    number = requests.get('http://number_api:5000/get_number')
    prompt = requests.post('http://prompt_api:5000/get_prompt', json)
    return render_template('index.html', word = word.text, number = number.text, )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)