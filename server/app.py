from flask import Flask, render_template
import requests
from os import getenv
from sqlalchemy import desc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')

db = SQLAlchemy(app)

class Challenges(db.model):
    id = db.Column(db.Integer, primary_key = True)
    word = db.Column(db.String(50), nullable = False)
    number = db.Column(db.Integer, nullable = False)
    prompt = db.Column(db.String(200), nullable = True)

@app.route('/')
def home():
    word = requests.get('http://word_api:5003/get_word')
    word_dict = word.json()
    number = requests.get('http://number_api:5001/get_number')
    number_dict = number.json()
    prompt = requests.post('http://prompt_api:5002/get_prompt', json = {"word": word_dict["word"], "num": number_dict["num"]})
    prompt_dict = prompt.json()

    recent_challenges = Challenges.query.order_by(desc(Challenges.id)).limit(5).all
    db.session.add(
        Challenges(
            word = word_dict["word"],
            number = number = number_dict["num"],
            prompt = prompt = prompt_dict["prompt"]
        )
    )
    db.session.commit()

    return render_template('index.html', word = word_dict["word"], number = number_dict["num"], prompt = prompt_dict["prompt"], recent_challenges = recent_challenges)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)