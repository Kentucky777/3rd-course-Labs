from flask import Blueprint, redirect, abort, render_template, request, make_response

lab3 = Blueprint('lab3',__name__)


@lab3.route('/lab3/')
def lab():
    name = ''
    if name:
        name = request.cookies.get('name')
    else:
        name = 'Анон'
    name_color = request.cookies.get('name_color')
    return render_template('/lab3/lab3.html', name=name, name_color=name_color)


@lab3.route('/lab3/cookie/')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie/')
def delcookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name')
    resp.set_cookie('age')
    resp.set_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    sex = request.args.get('sex')
    return render_template('/lab3/form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order/')
def order():
    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success/<int:price>')
def success(price):
    return render_template('/lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    back = request.args.get('back')
    size = request.args.get('size')
    if color or back or size:
        resp = make_response(redirect('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if back:
            resp.set_cookie('back', back)
        if size:
            resp.set_cookie('size', size)
        return resp

    color = request.cookies.get('color')
    back = request.cookies.get('back')
    size = request.cookies.get('size')
    resp = make_response(render_template('lab3/settings.html', color=color, back=back, size=size))
    return resp