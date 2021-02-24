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


if __name__ == '__main__':
    app.run(port=8080, debug=True)
