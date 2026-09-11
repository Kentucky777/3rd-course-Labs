from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.errorhandler(404)
def not_found(err):
    return "Нет такой страницы", 404


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