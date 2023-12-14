from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("button.html")


@app.route("/article", methods=["GET"])
def show_article():

    return render_template("article.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
