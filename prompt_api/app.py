from flask import Flask, request

app = Flask(__name__)

@app.route('/get_challenge', methods = ['POST'])
def get_challenge():
    challenge = ''
    if len(json["word"]) <= 3 or int(json["num"]) >= 10:
        challenge = random.choice(['while standing on one leg', 'while patting your head', 'while rubbing your belly'])
        return jasonify({"challenge": challenge})
    else:
        return jasonify({"challenge": challenge})