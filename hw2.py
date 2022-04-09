from flask import Flask

app = Flask(__name__)


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def result(nickname, level: int, rating: float):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h3>Претендента {nickname} на участие в миссии:</h3>
                    <div class="alert alert-success" role="alert">
                        Поздравляем! Ваш рейтинг после {level} этапа отбора
                    </div>
                    <h3>составляет {rating}!</h3>
                    <div class="alert alert-warning" role="alert">
                        Желаем удачи!
                    </div>
                  </body>
                </html>'''


@app.route('/choice/<planet_name>')
def result_new(planet_name: str):
    planet_name = planet_name.lower().capitalize()
    planets = {
        'Меркурий': ['Планета земной группы', 'наименьшая из планет земной группы',
                     'Названа в честь древнеримского бога торговли',
                     'Среднее расстояние Меркурия от Солнца чуть меньше 58 млн км',
                     'обращается вокруг Солнца за 88 земных суток'],
        'Венера': ['ты венера я юпитер', 'ты москва я питер',
                   'люди помогите дышать',
                   'ты венера я юпитер', 'ты москва я питер на одной орбите опять'],
        'Земля': ['Наша любимая Земля',
                  'Тут есть кошки!!!!!!',
                  'Мы любим кошек!!!!!!',
                  'Люди, поклоняйтесь кошкам!!!',
                  'Кошки!!!!'],
        'Марс': ['Эта планета близка к Земле',
                 'На ней много необходимых ресурсов',
                 'На ней есть вода и атмосфера',
                 'На ней есть небольшое магнитное поле',
                 'Наконец, она просто красива!'],
        'Юпитер': ['бла бла', 'моё', 'воображение', 'кажется', 'иссякло'],
        'Сатурн': ['вапкр', 'впапв', 'вапв', 'укнн', 'пкрер'],
        'Уран': ['ркерцкур', 'кркер', 'укц3уп', 'врого', 'й343пеку'],
        'Нептун': ['синенькая планета', 'прикольная))', 'из газа вроде', 'большая ещё', 'уцкеу'],
        'Плутон': ['Планета!!!!', 'мы его любим тоже!!', 'вркегг', 'екгкег', 'енкн'],
    }
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" 
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                            crossorigin="anonymous">
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Моё предложение: {planet_name}</h1>
                        <div class="alert alert-light" role="alert">
                          {planets[planet_name][0]}
                        </div>
                        <div class="alert alert-primary" role="alert">
                          {planets[planet_name][1]}
                        </div>
                        <div class="alert alert-danger" role="alert">
                          {planets[planet_name][2]}
                        </div>
                        <div class="alert alert-primary" role="alert">
                          {planets[planet_name][3]}
                        </div>
                        <div class="alert alert-warning" role="alert">
                          {planets[planet_name][4]}
                        </div>
                      </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')