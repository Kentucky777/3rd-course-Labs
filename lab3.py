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


@lab3.route('/lab3/ticket')
def ticket():
    errors = {}

    if 'fio' in request.args:
        fio = request.args.get('fio', '').strip()
        berth = request.args.get('berth', '').strip()
        linen = request.args.get('linen', '').strip()
        luggage = request.args.get('luggage', '').strip()
        age_str = request.args.get('age', '').strip()
        departure = request.args.get('departure', '').strip()
        destination = request.args.get('destination', '').strip()
        date = request.args.get('date', '').strip()
        insurance = request.args.get('insurance', '').strip()


        if not fio:
            errors['fio'] = 'Заполните ФИО'
        if not departure:
            errors['departure'] = 'Укажите пункт выезда'
        if not destination:
            errors['destination'] = 'Укажите пункт назначения'
        if not date:
            errors['date'] = 'Укажите дату поездки'

        age = None
        if not age_str:
            errors['age'] = 'Укажите возраст'
        else:
            try:
                age = int(age_str)
                if age < 1 or age > 120:
                    errors['age'] = 'Возраст должен быть от 1 до 120 лет'
            except ValueError:
                errors['age'] = 'Возраст должен быть числом'

        if not errors:
            is_child = age < 18
            price = 700 if is_child else 1000

            if berth in ['нижняя', 'нижняя боковая']:
                price += 100
            if linen == 'да':
                price += 75
            if luggage == 'да':
                price += 250
            if insurance == 'да':
                price += 150

            ticket_data = {
                'fio': fio,
                'age': age,
                'is_child': is_child,
                'berth': berth,
                'linen': linen,
                'luggage': luggage,
                'insurance': insurance,
                'departure': departure,
                'destination': destination,
                'date': date,
                'price': price
            }
            return render_template('lab3/ticket_success.html', ticket=ticket_data)

        return render_template('lab3/ticket_form.html', errors=errors, form=request.args)

    return render_template('lab3/ticket_form.html', errors={}, form={})


@lab3.route('/lab3/cleanc')
def clean():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('color')
    resp.set_cookie('back')
    resp.set_cookie('size')
    return resp