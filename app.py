from flask import Flask, url_for, request, redirect, abort, render_template
from lab1 import lab1
from lab2 import lab2
from werkzeug.exceptions import HTTPException
import datetime

app = Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
log = []
date = None
client_ip = None

class PaymentRequired(HTTPException):
    code = 402
    description = "Требуется оплата"

@app.before_request
def log_req():
    global client_ip
    global date
    time = datetime.datetime.today()
    client_ip = request.remote_addr
    date = time.date()
    url = request.url
    txt = f"{time}, пользователь {client_ip} заходил на адрес: {url}"
    log.append(txt)

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


@app.route("/cleanlog")
def clean_log():
    global log
    log = []
    return'''
<!doctype html>
<html>
    <body>
        <h1>Лог очищен!</h1>
        <p><a href="/">Главная</a></p>
    </body>
</html>
'''

@app.errorhandler(404)
def not_found(err):
    global log
    client_ip = request.remote_addr
    date = datetime.date.today()
    time = datetime.datetime.today()
    url = request.url
    client_ip = request.remote_addr
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
        <p>IP-адрес: ''' + client_ip + '''</p>
        <p>Дата посещения: ''' + str(date) + '''</p>
        <p><a href="/">Главная</a></p>
        <p><img src ="''' + url_for("static", filename="error.webp") + '''"</p>
        <p>Лог: ''' + '<br>'.join(log) + '''</p>
        <p><a href="/cleanlog">Очистить лог</a></p>
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


@app.errorhandler(500)
def c500(err):
    return '''
<!doctype html>
<html>
    <body>
        Была замечена ошибка в коде программы!
    </body>
</html>
''', 500, {
    'Content-Language': 'ru-RU'
}


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
        <a href="/lab1">Лаборатоная 1</a><br>
        <a href="/lab2">Лабораторная 2</a>
    </main>
    <footer>
        &copy; Байков Никита, ФБИ-41, 3 курс, 2026
    </footer>
    
</body>
</html>
'''