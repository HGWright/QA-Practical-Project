from flask import Flask, request

app = Flask(__name__)

@app.route('/get_challenge', methods = ['POST'])
def get_challenge():
    challenge = ''
    if len(get_word) <= 3 or int(get_number) >= 10:
        return challenge = random.choice(['while standing on one leg', 'while patting your head', 'while rubbing your belly'])
    else:
        return challenge