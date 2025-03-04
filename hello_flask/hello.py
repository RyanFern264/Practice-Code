from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper_function():
        html_string = function()
        bolded = "<b>" + html_string + "</b>"
        return bolded
    return wrapper_function


@app.route("/")
def hello_world():
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>This is a paragraph</p>"
            "<img src='https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExYXVremZiZXhvaGdmMjMza2ttOHEyNGJsczZvcHI2dXF1OWZ2Ynp2eCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tqDKjJwTlVKceq4ToH/giphy.gif'>")


@app.route("/bye")
@make_bold
def bye_world():
    return "<p>Bye</p>"

@app.route("/<name>")
def greet(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)

