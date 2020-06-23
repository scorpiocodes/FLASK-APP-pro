from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/<string:name>")
def custom(name):
    return render_template('custom.html', name = name)

if __name__ == '__main__':
    app.run(debug=True)