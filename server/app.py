from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    word = requests.get('http://word_api:5000/get_word')
    number = requests.get('http://number_api:5000/get_number')
    prompt = requests.post('http://prompt_api:5000/get_prompt', )
    return render_template('index.html', word = word.text, number = number.text, )