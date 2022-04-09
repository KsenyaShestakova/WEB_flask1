import os
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        photo = request.files['file']
        photo.filename = 'load_photo.jpg'
        photo.save(f'./static/img/{photo.filename}')
    if os.path.exists("./static/img/load_photo.jpg"):
        return render_template('2.html')
    return render_template('2_base.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    os.remove('./static/img/load_photo.jpg')