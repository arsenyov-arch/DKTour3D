from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index_page():
    return render_template("Home.html")

@app.route("/kvant")
def kvant_page():
    return render_template("KVANT.html")

@app.route("/dzhd")
def dzhd_page():
    return render_template("DZHD.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")