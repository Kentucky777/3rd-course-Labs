from flask import Blueprint, render_template, request, redirect, session
import psycopg2
from psycopg2.extras  import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
lab5 = Blueprint('lab5', __name__)

@lab5.route('/lab5')
def lab():
    return render_template('lab5/lab5.html', login=session.get('login'))


@lab5.route('/lab5/register', methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('lab5/register.html')

    login = request.form.get('login')
    real_name  = request.form.get('real_name')
    password = request.form.get('password')

    if not login or not password or not real_name:
        return render_template('lab5/register.html', error='Заполните все поля')
    
    conn, cur = db_connect()
                
    cur.execute(f"select login from users where login=%s;", (login, ))
    if cur.fetchone():
        db_close(conn,cur)
        return render_template('lab5/register.html', error='Такой пользователь уже существует')
    password_hash = generate_password_hash(password)
    cur.execute(f"insert into users (login, real_name, password) values (%s, %s, %s);", (login, real_name, password_hash))
    db_close(conn,cur)
    return render_template('lab5/success.html', login=login)


@lab5.route('/lab5/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('lab5/login.html')
    login = request.form.get('login')
    password = request.form.get('password')

    if not (login or password):
        return render_template('lab5/login.html', error = 'Заполните все поля')

    conn, cur = db_connect()

    cur.execute(f"select * from users where login = %s;", (login, ))
    user = cur.fetchone()

    if not user:
        db_close(conn, cur)
        return render_template('lab5/login.html', error='Логин и/или пароль неверны')

    if not check_password_hash(user['password'], password):
        db_close(conn, cur)
        return render_template('lab5/login.html', error='Логин и/или пароль неверны')

    session['login'] = login
    db_close(conn, cur)
    return render_template('lab5/success_login.html', login=login)


def db_connect():
    conn = psycopg2.connect(
            host = '127.0.0.1',
            database = 'nikita_baykov_knowledge_base',
            user = 'nikita_baykov_knowledge_base',
            password = '123'          
        )
    cur = conn.cursor(cursor_factory= RealDictCursor)

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


@lab5.route('/lab5/create', methods = ['GET', 'POST'])
def create():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    if request.method == 'GET':
        return render_template('lab5/create_article.html')
    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_favorite = bool(request.form.get('is_favorite'))
    is_public = bool(request.form.get('is_public'))

    if not title or not article_text:
        return 'Вы не ввели название или текст статьи!'
    conn, cur = db_connect()

    cur.execute("select * from users where login=%s;", (login, ))
    login_id = cur.fetchone()["id"]

    cur.execute(f"insert into articles(login_id, title, article_text, is_favorite, is_public) values (%s, %s, %s, %s, %s);", (login_id, title, article_text, is_favorite, is_public))

    db_close(conn, cur)
    return redirect('/lab5')


@lab5.route('/lab5/list')
def list():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    cur.execute(f"select id from users where login=%s;", (login, ))
    login_id = cur.fetchone()["id"]

    cur.execute(f"select * from articles where login_id = %s order by is_favorite DESC, id DESC;", (login_id, ))
    articles = cur.fetchall()
    if not articles:
            return render_template('lab5/articles.html', error = 'Не найдено ни одной статьи!')

    db_close(conn, cur)
    return render_template('lab5/articles.html', articles=articles)


@lab5.route('/lab5/logout')
def logout():
    session.pop('login', None)
    return redirect('/lab5')


@lab5.route('/lab5/edit/<int:article_id>', methods=['GET', 'POST'])
def edit_article(article_id):
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    cur.execute("SELECT id FROM users WHERE login=%s;", (login, ))
    user = cur.fetchone()
    login_id = user["id"]

    cur.execute("SELECT * FROM articles WHERE id=%s AND login_id=%s;", (article_id, login_id))
    article = cur.fetchone()

    if not article:
        db_close(conn, cur)
        return redirect('/lab5/list')

    if request.method == 'GET':
        db_close(conn, cur)
        return render_template('lab5/edit_article.html', article=article)

    title = request.form.get('title')
    article_text = request.form.get('article_text')
    is_favorite = bool(request.form.get('is_favorite'))
    is_public = bool(request.form.get('is_public'))

    if not title or not article_text:
        db_close(conn, cur)
        return render_template('lab5/edit_article.html', article=article, error='Заполните все поля!')

    cur.execute("UPDATE articles SET title=%s, article_text=%s, is_favorite=%s, is_public=%s WHERE id=%s AND login_id=%s;",(title, article_text, is_favorite, is_public, article_id, login_id))

    db_close(conn, cur)
    return redirect('/lab5/list')


@lab5.route('/lab5/delete/<int:article_id>')
def delete_article(article_id):
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()

    cur.execute("SELECT id FROM users WHERE login=%s;", (login, ))
    login_id = cur.fetchone()["id"]

    cur.execute("DELETE FROM articles WHERE id=%s AND login_id=%s;", (article_id, login_id))

    db_close(conn, cur)
    return redirect('/lab5/list')

@lab5.route('/lab5/users')
def users_list():
    conn, cur = db_connect()
    cur.execute("SELECT login, real_name FROM users ORDER BY id;")
    users = cur.fetchall()
    db_close(conn, cur)
    return render_template('lab5/users.html', users=users)


@lab5.route('/lab5/profile', methods=['GET', 'POST'])
def profile():
    login = session.get('login')
    if not login:
        return redirect('/lab5/login')

    conn, cur = db_connect()
    cur.execute("SELECT id, login, real_name FROM users WHERE login=%s;", (login, ))
    user = cur.fetchone()

    if request.method == 'GET':
        db_close(conn, cur)
        return render_template('lab5/profile.html', user=user)

    real_name = request.form.get('real_name')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    if not real_name:
        db_close(conn, cur)
        return render_template('lab5/profile.html', user=user, error='Имя не может быть пустым')

    if password or confirm_password:
        if password != confirm_password:
            db_close(conn, cur)
            return render_template('lab5/profile.html', user=user, error='Пароли не совпадают')
        password_hash = generate_password_hash(password)
        cur.execute(
            "UPDATE users SET real_name=%s, password=%s WHERE login=%s;",
            (real_name, password_hash, login)
        )
    else:
        cur.execute(
            "UPDATE users SET real_name=%s WHERE login=%s;",
            (real_name, login)
        )

    db_close(conn, cur)
    return redirect('/lab5')


@lab5.route('/lab5/public')
def public_articles():
    conn, cur = db_connect()
    cur.execute("""
        SELECT articles.*, users.login AS author_login, users.real_name AS author_name
        FROM articles
        JOIN users ON articles.login_id = users.id
        WHERE articles.is_public = TRUE
        ORDER BY articles.is_favorite DESC, articles.id DESC;
    """)
    articles = cur.fetchall()
    db_close(conn, cur)

    if not articles:
        return render_template('lab5/public_articles.html', error='Публичных статей пока нет!')

    return render_template('lab5/public_articles.html', articles=articles)