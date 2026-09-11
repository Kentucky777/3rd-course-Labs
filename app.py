from flask import Flask, url_for, request, redirect, abort
from werkzeug.exceptions import HTTPException
import datetime

app = Flask(__name__)

class PaymentRequired(HTTPException):
    code = 402
    description = "Требуется оплата"


@app.route("/400")
def route400():
    abort(400)


@app.route("/401")
def route401():
    abort(401)


@app.route("/402")
def route402():
    raise PaymentRequired


@app.route("/403")
def route403():
    abort(403)


@app.route("/405")
def route405():
    abort(405)


@app.route("/418")
def route418():
    abort(418)


@app.errorhandler(404)
def not_found(err):
    return '''
<!doctype html>
<html>
<head>
    <style>
        body{
        color : red;
        background-color: black
        }
        img{
        height: 400px;
        weight: 600px;
        }
    </style>
</head>
    <body>
        <h1>Страница не найдена</h1>
        <p><img src ="''' + url_for("static", filename="error.webp") + '''"</p>
    </body>
</html>
''', 404


@app.errorhandler(400)
def c400(err):
    return "Неверный запрос", 400


@app.errorhandler(401)
def c401(err):
    return "Неавторизованный запрос", 401


@app.errorhandler(PaymentRequired)
def c402(err):
    return "Необходима оплата", 402


@app.errorhandler(403)
def c403(err):
    return "Запрещено", 403


@app.errorhandler(405)
def c405(err):
    return "Метод не разрешён", 405


@app.errorhandler(418)
def c418(err):
    return "Шутливый код", 418


@app.route("/")
@app.route("/index")
def main():
    return '''
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Байков Никита Дмитриевич. Лабораторная 1</title>
</head>
<body>
    <header>
        НГТУ, ФБ, WEB-программирование часть 2, Лабораторная 1
    </header>
    <main>
        <a href="/lab1">Лаборатоная 1</a>
    </main>
    <footer>
        &copy; Байков Никита, ФБИ-41, 3 курс, 2026
    </footer>
    
</body>
</html>
'''


@app.route("/lab1")
def citata():
    return '''
<!doctype html>
<html>
    <head>
        <title>Лабораторная 1</title>
    </head>
    <body>
        <h1>«Человек он умный, но чтоб умно поступать — одного ума мало».</h1>
        <p>Фёдор Достоевский</p>
        <p><a href="/">Главная</a></p>
    </body>
</html>
'''


@app.route("/lab1/web")
def start():
    return """<!doctype html>
        <html>
           <body>
               <h1> web-сервер на Flask</h1>
               <p><a href="/lab1/author">Автор</a></p>
               <p><a href="/lab1/image">Слон</a></p>
               <p><a href="/lab1/count">Счетчик и данные</a></p>
               <p><a href="/lab1/created">Создание</a></p>
           <body>
        <html>""", 200, {
            'X-server': 'sample',
            'Content-Type' : 'text/html; charset=utf-8'
        }


@app.route("/lab1/author")
def author():
    name = "Байков Никита Дмитриевич"
    group = "ФБИ-41"
    faculty = "ФБ"

    return """<!doctype html>
        <html>
            <body>
            <p> Студент: """ + name + """</p>
            <p> Группа : """ + group + """</p>
            <p> Факультет: """ + faculty + """
            <p><a href="/lab1/web">web</a></p>
            </body>
        </html>"""


@app.route('/lab1/image')
def image():
    path = url_for("static", filename = 'elephant.jpg')
    return '''
<!doctype html>
<html>
<head>
    <link rel="stylesheet" href="'''  + url_for('static', filename='lab1.css') + '''">
</head>
    <body>
        <h1>Слон</h1>
        <img src="''' + path + '''">
    </body>
</html>'''

count = 0 

@app.route('/lab1/count')
def counter():
    global count
    count += 1
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
    return '''
<!doctype html>
<html>
    <body>
        Сколько раз вы сюда заходили ''' + str(count) + '''
        <hr>
        <p>Дата и время : ''' + str(time) + '''</p>
        <p>Запрошенный адрес : ''' + url + '''</p>
        <p>IP-адрес клиента : ''' + client_ip + '''</p>
        <p><a href="/lab1/cleaner">Очистить счётчик</a></p>
    </body>
</html>
'''


@app.route("/lab1/cleaner")
def cleaner():
    global count
    count = 0
    return '''
<!doctype html>
<html>
    <body>
        <p>Счётчик отчищен!</p>
        <p><a href="/lab1/count">Вернуться к информации</a></p>
    </body>
</html>
'''


@app.route("/lab1/info")
def info():
    return redirect("/lab1/author")


@app.route("/lab1/created")
def created():
    return '''
<!doctype html>
<html>
    <body>
        <h1>Создано успешно</h1>
        <div><i>Что - то создано...</i></div>
    </body>
</html>
''', 201