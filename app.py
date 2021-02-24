from flask import Flask, render_template
from forms import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '2876ba4f8b2cc5013a990873c061e634'


@app.route("/<title>")
@app.route("/index/<title>")
def root(title):
    return render_template("mission.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    return render_template(
        "training.html", title="Тренировка", prof=prof.lower())


@app.route("/list_prof/<list>")
def list_prof(list):
    return render_template(
        "list_prof.html", title="Список профессий", list=list)


@app.route("/answer")
@app.route("/auto_answer")
def answer():
    data = {
        "title": "Анкета",
        "surname": "Watny",
        "name": "Mark",
        "education": "выше среднего",
        "profession": "штурман марсохода",
        "sex": "male",
        "motivation": "Всегда мечтал застрять на Марсе!",
        "ready": True
    }
    return render_template("auto_answer.html", data=data)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template("login.html", form=form, title="Аварийный доступ")


if __name__ == '__main__':
    app.run(port=8080, debug=True)
