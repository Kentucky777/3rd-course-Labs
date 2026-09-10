from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/web")
def start():
    return """<!docktype html>
        <html>
           <body>
               <h1> web-сервер на Flask</h1>
               <p><a href="/author">Автор</a></p>
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