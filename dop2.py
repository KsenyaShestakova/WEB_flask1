import os
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/load_photo', methods=['GET'])
def load_photo():
    return render_template('dop2.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')