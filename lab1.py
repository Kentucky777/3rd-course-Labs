from flask import Blueprint, url_for, request, redirect
import datetime

lab1 = Blueprint('lab1',__name__)
@lab1.route('/lab1/fail')
def fail():
    return 1 / 0

@lab1.route("/lab1")
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
        <h2>Меню</h2>
        <p><a href="/lab1/author">Автор</a></p>
        <p><a href="/lab1/image">Слон</a></p>
        <p><a href="/lab1/count">Счетчик и данные</a></p>
        <p><a href="/lab1/created">Создание</a></p>
        <p><a href="/lab1/image2">Elephant</a></p>
        <p><a href="/lab1/image3">Elefant</a></p>
        <p><a href="/lab1/cleaner">Очистка</a></p>
        <p><a href="/lab1/info">Информация</a></p>
        <p><a href="/lab1/web">web</a></p>
        <p><a href="/400">Ошибка 400</a></p>
        <p><a href="/401">Ошибка 401</a></p>
        <p><a href="/402">Ошибка 402</a></p>
        <p><a href="/403">Ошибка 403</a></p>
        <p><a href="/404">Ошибка 404</a></p>
        <p><a href="/405">Ошибка 405</a></p>
        <p><a href="/418">Ошибка 418</a></p>
        <p><a href="/lab1/fail">Ошибка 500</a></p>
    </body>
</html>
'''


@lab1.route("/lab1/web")
def start():
    return """<!doctype html>
        <html>
           <body>
               <h1> web-сервер на Flask</h1>
           <body>
        <html>""", 200, {
            'X-server': 'sample',
            'Content-Type' : 'text/html; charset=utf-8'
        }


@lab1.route("/lab1/author")
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


@lab1.route('/lab1/image')
def image():
    path = url_for("static", filename = 'lab1/elephant.jpg')
    return '''
<!doctype html>
<html>
<head>
    <link rel="stylesheet" href="'''  + url_for('static', filename='lab1/lab1.css') + '''">
</head>
    <body>
        <h1>Слон</h1>
        <img src="''' + path + '''">
    </body>
</html>''', {'Content-Language': 'ru-RU',
             'X-image' : 'slon',
             'X-prost' : 'prosto'
        }


@lab1.route('/lab1/image2')
def image2():
    path = url_for("static", filename = 'lab1/elephant.jpg')
    return '''
<!doctype html>
<html>
<head>
    <link rel="stylesheet" href="'''  + url_for('static', filename='lab1/lab1.css') + '''">
</head>
    <body>
        <h1>Elephant</h1>
        <img src="''' + path + '''">
    </body>
</html>''', {'Content-Language': 'en-EN',
             'X-image' : 'slon',
             'X-prost' : 'prosto'
        }


@lab1.route('/lab1/image3')
def image3():
    path = url_for("static", filename = 'lab1/elephant.jpg')
    return '''
<!doctype html>
<html>
<head>
    <link rel="stylesheet" href="'''  + url_for('static', filename='lab1/lab1.css') + '''">
</head>
    <body>
        <h1>Elefant</h1>
        <img src="''' + path + '''">
    </body>
</html>''', {'Content-Language': 'de-DE',
             'X-image' : 'slon',
             'X-prost' : 'prosto'
        }

count = 0 

@lab1.route('/lab1/count')
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


@lab1.route("/lab1/cleaner")
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


@lab1.route("/lab1/info")
def info():
    return redirect("/lab1/author")


@lab1.route("/lab1/created")
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