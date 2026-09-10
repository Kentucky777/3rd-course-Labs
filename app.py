from flask import Flask, url_for, request, redirect
import datetime
app = Flask(__name__)

@app.route("/")
@app.route("/web")
def start():
    return """<!docktype html>
        <html>
           <body>
               <h1> web-сервер на Flask</h1>
               <p><a href="/author">Автор</a></p>
               <p><a href="/image">Слон</a></p>
               <p><a href="/count">Счетчик и данные</a></p>
           <body>
        <html>"""


@app.route("/author")
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
            <p><a href="/web">web</a></p>
            </body>
        </html>"""


@app.route('/image')
def image():
    path = url_for("static", filename = 'elephant.jpg')
    return '''
<!doctype html>
<html>
    <body>
        <h1>Слон</h1>
        <img src="''' + path + '''">
    </body>
</html>'''

count = 0 

@app.route('/count')
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
    </body>
</html>
'''
@app.route("/info")
def info():
    return redirect("/author")