from flask import Flask
from random import randint

app = Flask(__name__)

@app.route("/")
def guess():
    return("<h1>Guess the number between 0 and 9</h1>"
           "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExb25kMGh3cXhoZWM1djJnN2MwY2lscXRicGRjbW9hbGl3ZDI5NDY4eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YnVON2WUV2kDULk0hz/giphy.gif'>")

target_num = randint(0,9)

@app.route("/<user_number>")
def guess_num(user_number):
    user_number = int(user_number)
    if user_number < target_num:
        return "Too low!"
    elif user_number > target_num:
        return "Too high!"
    else:
        return "yeah!"

if __name__ == "__main__":
    app.run(debug=True)