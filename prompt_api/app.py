from flask import Flask, request

app = Flask(__name__)

@app.route('/get_challenge', methods = ['POST'])
def get_challenge():
    challenge = ''
    if len(get_word) <= 3 or int(get_number) >= 10:
        return challenge = random.choice(['stand on one leg', 'pat your head'])
    else:
        return challenge