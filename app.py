import os
from flask import Flask, render_template


app = Flask(__name__)

app.secret_key = os.urandom(12).hex()
# app.config['SERVER_NAME'] = 'localhost:5000'


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
