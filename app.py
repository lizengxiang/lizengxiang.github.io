from flask import Flask, render_template
from flask import request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources=r'/*')


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
