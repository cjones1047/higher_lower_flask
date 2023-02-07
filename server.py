from flask import Flask

app = Flask(__name__)


# print(__name__)


@app.route('/')
def have_user_guess():
    return ('<h1>Guess a number between 0 and 9...</h1>'
            '<img src="https://media4.giphy.com/media/JdFEeta1hLNnO/200w.gif?'
            'cid=6c09b952w1haa2yf997i4f8d4xeht2gzq1eag72imrchh3qc&rid=200w.gif&ct=g">')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
