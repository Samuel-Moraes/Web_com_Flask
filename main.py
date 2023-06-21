from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cadastro')
def cadastro():
    return render_template("cadastro.html")


app.run()

if __name__ == "__main__":
    app.run(debug=True)