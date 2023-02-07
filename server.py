from flask import Flask
import random

app = Flask(__name__)
secret_num = None
text_align = "text-align: center;"
red_text = "color: red"
green_text = "color: green"
gif_width = 800


# print(__name__)


@app.route('/')
def have_user_guess():
    global secret_num
    secret_num = random.randint(1, 10)
    print(secret_num)
    return (f'<h1 style="{text_align}">Guess a number between 0 and 9...</h1>'
            f'<div style="{text_align}">'
            f'<img src="https://media4.giphy.com/media/JdFEeta1hLNnO/200w.gif?'
            f'cid=6c09b952w1haa2yf997i4f8d4xeht2gzq1eag72imrchh3qc&rid=200w.gif&ct=g" width={gif_width}>'
            f'</div>')


@app.route('/<int:guess>')
def check_guess(guess):
    if guess > secret_num:
        return (f'<div style="{text_align}">'
                f'<h1 style="color: red">{guess} is TOO HIGH</h1>'
                f'<img src="https://media.tenor.com/ygwcx5jLLmsAAAAM/seinfeld-kramer.gif" width={gif_width}>'
                f'</div>')

    elif guess < secret_num:
        return (f'<div style="{text_align}">'
                f'<h1 style="color: red">{guess} is TOO LOW</h1>'
                f'<img src="https://media.tenor.com/u-2k8TCqbCcAAAAM/really-low-neil-degrasse-tyson.gif" '
                f'width={gif_width}>'
                f'</div>')
    else:
        return (f'<div style="{text_align}">'
                f'<h1 style="color: green">{guess} is CORRECT</h1>'
                f'<img src="https://media.tenor.com/ynST0DWtFqgAAAAC/pointing-that-is-correct.gif" width={gif_width}>'
                f'</div>')


if __name__ == "__main__":
    app.run(port=8000, debug=True)
