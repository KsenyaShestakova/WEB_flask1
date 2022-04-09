import os

import jinja2
from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "Привет, Яндекс!"


@app.route('/countdown')
def countdown():
    countdown_list = [str(x) for x in range(10, 0, -1)]
    countdown_list.append('Пуск!')
    return '</br>'.join(countdown_list)


@app.route('/image_sample')
def image():
    return f'''<img src="{url_for('static', filename='img/riana.jpeg')}" 
           alt="здесь должна была быть картинка, но не нашлась">'''


@app.route('/sample_page')
def return_sample_page():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_form.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


@app.route('/bootstrap_sample')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Привет, Яндекс!</h1>
                    <div class="alert alert-primary" role="alert">
                      А мы тут компонентами Bootstrap балуемся
                    </div>
                  </body>
                </html>'''


@app.route('/greeting/<username>')
def greeting(username):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                   <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Привет, {username}</title>
                  </head>
                  <body>
                    <h1>Привет, {username}!</h1>
                  </body>
                </html>'''


@app.route('/two_params/<username>/<int:number>')
def two_params(username, number):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                   href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                   integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                   crossorigin="anonymous">
                    <title>Пример с несколькими параметрами</title>
                  </head>
                  <body>
                    <h2>{username}</h2>
                    <div>Это первый параметр и его тип: {str(type(username))[1:-1]}</div>
                    <h2>{number}</h2>
                    <div>Это второй параметр и его тип: {str(type(number))[1:-1]}</div>
                  </body>
                </html>'''


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_form.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="middle">Анкета претендента</h1>
                            <h2 align="middle">на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnameHelp"
                                    placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" aria-describedby="namelHelp"
                                    placeholder="Введите имя" name="name">
                                    <p></p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                                    placeholder="Введите адрес электронной почты" name="email">
                                    <p></p>
                                    <div class="form-group">
                                        <label for="eduSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="edu">
                                          <option>Базовое</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее специальное</option>
                                          <option>Среднее полное</option>
                                          <option>Высшее</option>
                                          <option>Наивысшее</option>
                                        </select>
                                     </div>
                                     <p></p>
                                    <label for="profSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof">
                                      <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                      <br>
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof1">
                                      <label class="form-check-label" for="acceptRules">пилот</label>
                                      <br>
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof2">
                                      <label class="form-check-label" for="acceptRules">учитель</label>
                                      <br>
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof3">
                                      <label class="form-check-label" for="acceptRules">астролог</label>
                                      <br>
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof4">
                                      <label class="form-check-label" for="acceptRules">врач</label>
                                      <br>
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof5">
                                      <label class="form-check-label" for="acceptRules">оператор-марсохода</label>                                            
                                    </div>
                                    <div class="form-group">
                                    <p></p>
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <p></p>
                                    <div class="form-group">
                                        <label for="about">Зачем вам все это????</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <p></p>
                                    <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <p></p>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form)
        print(request.form.get('surname', None))
        print(request.form.get('name', None))
        print(request.form.get('email', None))
        print(request.form.get('edu', None))
        print(request.form.get('file', None))
        print(request.form.get('about', None))
        print(request.form.get('sex', None))
        print(request.form.get('prof', None))
        print(request.form.get('prof1', None))
        print(request.form.get('prof2', None))
        print(request.form.get('prof3', None))
        print(request.form.get('prof4', None))
        print(request.form.get('prof5', None))
        return "Форма отправлена"


@app.route('/load_photo', methods=['POST', 'GET'])
def load_photo():
    if request.method == 'POST':
        file1 = request.files['file']
        file1.filename = 'load_photo.jpg'
        path = os.path.join('./static/img', file1.filename)
        file1.save(path)
        return render_template('2.html')
    elif request.method == 'GET':
        try:
            return render_template('2.html')
        except jinja2.exceptions.TemplateNotFound:
            return render_template('2_base.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')