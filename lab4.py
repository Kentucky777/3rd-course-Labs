from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('/lab4/lab4.html')


@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')


@lab4.route('/lab4/div', methods = ['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены')
    elif int(x2) == 0:
        return render_template('lab4/div.html', error='Деление на ноль невозможно!')
    else:
        x1 = int(x1)
        x2 = int(x2)
        result = x1 / x2 
        return render_template('lab4/div.html',x1=x1,x2=x2,result=result)


@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')


@lab4.route('/lab4/sum', methods = ['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = '0'
    if x2 == '':
        x2 = '0'
    x1 = int(x1)
    x2 = int(x2)
    result = x1 + x2 
    return render_template('lab4/sum.html',x1=x1,x2=x2,result=result)


@lab4.route('/lab4/multi-form')
def multi_form():
    return render_template('lab4/multi-form.html')


@lab4.route('/lab4/multi', methods = ['POST'])
def multi():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '':
        x1 = '1'
    if x2 == '':
        x2 = '1'
    x1 = int(x1)
    x2 = int(x2)
    result = x1 * x2 
    return render_template('lab4/multi.html',x1=x1,x2=x2,result=result)


@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')


@lab4.route('/lab4/sub', methods = ['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены')
    else:
        x1 = int(x1)
        x2 = int(x2)
        result = x1 - x2 
        return render_template('lab4/sub.html',x1=x1,x2=x2,result=result)


@lab4.route('/lab4/exp-form')
def exp_form():
    return render_template('lab4/exp-form.html')


@lab4.route('/lab4/exp', methods = ['POST'])
def exp():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/exp.html', error='Оба поля должны быть заполнены')
    elif int(x2) == 0 and int(x1) == 0:
        return render_template('lab4/exp.html', error='Возведение двух 0 невозможно!')
    else:
        x1 = int(x1)
        x2 = int(x2)
        result = x1 ** x2 
        return render_template('lab4/exp.html',x1=x1,x2=x2,result=result)


tree_count = 0

@lab4.route('/lab4/tree', methods=['GET','POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')
        
    if operation == 'cut':
        tree_count -= 1
    elif operation == 'plant':
        tree_count += 1

    if tree_count < 0 :
            tree_count = 0
            return '''Ошибка!'''
    return redirect('/lab4/tree')


users = [
    {'login': 'alex', 'password': '123', 'name': 'Алексей', 'gender':'мужской'},
    {'login': 'bob', 'password': '555', 'name': 'Боб','gender': 'мужской'},
    {'login': 'katya', 'password': '228', 'name': 'Катя', 'gender': 'женский'},
    {'login':'nikita', 'password':'777', 'name': 'Никита', 'gender':'мужской'},
]


@lab4.route('/lab4/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            name = session['name']
        else:
            authorized = False
            name = ''
        return render_template('lab4/login.html', authorized=authorized, login='', name=name)
    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введен логин'
        return render_template('lab4/login.html', error=error, login=login)

    if not password:
            error = 'Не введен пароль'
            return render_template('lab4/login.html', error=error, login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login
            session['name'] = user['name']
            session['gender'] = user['gender']
            return redirect('/lab4/login')

    error = 'Неверные логин или пароль'
    return render_template('lab4/login.html', error=error, login=login)


@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    session.pop('name', None)
    session.pop('gender', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/weather', methods=['GET','POST'])
def weather():
    if request.method == 'GET':
        return render_template('lab4/weather.html')
    
    temperature = int(request.form.get('temperature'))

    if not temperature:
        error = 'Не введена темпрература'
        return render_template('lab4/weather.html', error=error)

    if temperature < -30:
        result = 'слишком холодно'

    elif temperature <= -30:
        result = 'слишком жарко'

    elif -30 <= temperature <= -15:
        result = 'Очень холодно'

    elif -14 <= temperature <= 0:
        result = 'Холодно'

    elif 1 <= temperature <= 15:
        result = 'Прохладно'

    elif 16 <= temperature <= 25:
        result = 'Тепло'

    elif 26 <= temperature <= 30:
        result = 'Жарко'
    else:
        result = 'Слишком жарко'
    
    return render_template('lab4/weather.html', result=result, temperature=temperature)


@lab4.route('/lab4/order', methods=['GET', 'POST'])
def order():
  prices = {'М200': 4200, 'М300': 4800, 'М400': 5400, 'М500': 6100}

  if request.method == 'GET':
    return render_template('lab4/order.html', type='М200', prices=prices)

  type = request.form.get('type', 'М200')
  volume = request.form.get('volume')
  volume = int(volume)

  if not volume:
    error = 'Ошибка: не указан объём бетона'
    return render_template('lab4/order.html', error=error, type=type, volume=volume, prices=prices)

  if volume <= 0:
    error = 'объём бетона должен быть больше нуля'
    return render_template('lab4/order.html', error=error, type=type, volume=volume, prices=prices)

  if volume > 100:
    error = 'Такого объёма сейчас нет в наличии'
    return render_template('lab4/order.html', error=error, type=type, volume=volume, prices=prices)

  price_per_m3 = prices.get(type, 4200)
  total = volume * price_per_m3
  discount_applied = False
  discount_amount = 0

  if volume > 10:
    discount_applied = True
    discount_amount = total * 0.10
    total_price = total - discount_amount

  else:
    total_price = total

  return render_template('lab4/order.html', success=True, type=type, volume=volume, total_price=total_price, discount_applied=discount_applied, discount_amount=discount_amount, prices=prices)


@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
  if request.method == 'GET':
    return render_template('lab4/register.html')

  login = request.form.get('login')
  name = request.form.get('name')
  password = request.form.get('password')
  confirm = request.form.get('password_confirm')
  gender = request.form.get('gender')

  if not login:
    return render_template('lab4/register.html', error='Не введён логин', login=login, name=name)
  if not name:
    return render_template('lab4/register.html', error='Не введено имя', login=login, name=name,
    )
  if not password:
    return render_template('lab4/register.html', error='Не введён пароль', login=login, name=name)
  if password != confirm:
    return render_template('lab4/register.html', error='Пароли не совпадают', login=login, name=name)

  users.append({
      'login': login,
      'password': password,
      'name': name,
      'gender': gender,
  })

  return redirect('/lab4/login')


@lab4.route('/lab4/users', methods=['GET', 'POST'])
def users_list():
  if 'login' not in session:
    return redirect('/lab4/login')

  current_user = next(
      (u for u in users if u['login'] == session['login']), None
  )
  if not current_user:
    session.clear()
    return redirect('/lab4/login')

  error = None

  if request.method == 'POST':
    new_login = request.form.get('login')
    new_name = request.form.get('name')
    new_password = request.form.get('password')
    confirm_password = request.form.get('password_confirm')

    if not new_login:
      error = 'Логин не может быть пустым'
    elif not new_name:
      error = 'Имя не может быть пустым'
    elif (
        new_login != current_user['login']
        and any(u['login'] == new_login for u in users)
    ):
      error = 'Пользователь с таким логином уже существует'
    elif new_password or confirm_password:
      if new_password != confirm_password:
        error = 'Пароли не совпадают'
      else:
        current_user['password'] = new_password

    if not error:
      current_user['login'] = new_login
      current_user['name'] = new_name
      session['login'] = new_login
      session['name'] = new_name
      return redirect('/lab4/users')

  safe_users = [
      {'login': u['login'], 'name': u['name'], 'gender': u.get('gender')}
      for u in users
  ]

  return render_template('lab4/users.html', users=safe_users, current_user={
          'login': current_user['login'],
          'name': current_user['name'],
      }, error=error)


@lab4.route('/lab4/users/delete', methods=['POST'])
def delete_user():
  if 'login' not in session:
    return redirect('/lab4/login')

  current_login = session['login']
  for i, u in enumerate(users):
    if u['login'] == current_login:
      del users[i]
      break

  session.pop('login', None)
  session.pop('name', None)
  session.pop('gender', None)
  return redirect('/lab4/login')