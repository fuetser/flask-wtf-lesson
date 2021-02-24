from flask import Flask, render_template


app = Flask(__name__)


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
    print(list)
    return render_template(
        "list_prof.html", title="Список профессий", list=list)


if __name__ == '__main__':
    app.run(port=8080, debug=True)
