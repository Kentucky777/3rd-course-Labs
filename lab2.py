from flask import Blueprint, redirect, abort, render_template


lab2 = Blueprint('lab2',__name__)


@lab2.route("/lab2/a")
def a():
    return 'без слэша'


@lab2.route("/lab2/a/")
def a2():
    return 'со слэшем'


flower_list = [
    {'name':'роза', 'price': 120}, 
    {'name':'тюльпан', 'price': 150},
    {'name':'незабудка','price': 90},
    {'name':'ромашка','price': 50}
    ]
@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        abort(404)
    else:
        f_lower = flower_list[flower_id]
        return render_template('lab2/flowerslist.html', f_lower=f_lower)


@lab2.route('/lab2/add_flower/<name>/<int:price>')
def add_flowers(name,price):
    flower_list.append({'name':name,'price':price})
    fl_len = len(flower_list)
    return render_template('lab2/floweradd.html', flower_list=flower_list, name=name, fl_len = fl_len, price=price)


@lab2.route('/lab2/add_flower/<name>/')
def noprice(name):
    return 'Вы не ввели цену!'


@lab2.route('/lab2/del_flower/<int:id>')
def del_fl(id):
    if id > len(flower_list) or id == 0:
        abort(404) 
    else:
        del flower_list[id-1]
        return render_template('lab2/flowerdel.html', id = id)


@lab2.route('/lab2/flowers/')
def flowers_list():
    global flower_list
    len_f = len(flower_list)
    return render_template('lab2/flowers.html', len_f=len_f, flower_list=flower_list)

@lab2.route('/lab2/sortname/')
def sortname():
    flower_list.sort(key= lambda x: x['name'])
    return render_template('lab2/sortname.html')

@lab2.route('/lab2/sortprice/')
def sortprice():
    flower_list.sort(key= lambda x: x['price'])
    return render_template('lab2/sortprice.html')


@lab2.route('/lab2/cleanfl/')
def clean():
    global flower_list
    flower_list.clear()
    return f'''
<!doctype html>
<html>
<body>
    <div>Список очищен</div>
    <a href="/lab2/flowers">Цветы</a>
</body>
</html>
'''


@lab2.route('/lab2/example/')
def example():
    name = 'Байков Никита'
    number = '2'
    group = 'ФБИ-41'
    course = '3 курс'
    fruits = [
        {'name':'яблоки', 'price' : 100},
        {'name':'апельсины', 'price' : 120},
        {'name':'груши', 'price' : 80},
        {'name':'мандарины', 'price' : 95},
        {'name':'манго', 'price' : 321}
    ]
    return render_template('lab2/example.html', name = name, number = number, group=group, course=course, fruits=fruits)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/filters/')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase=phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a,b):
    return render_template('lab2/calc.html', a=a, b=b)


@lab2.route('/lab2/calc/')
def redir():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
def redir2(a):
    return redirect(f'/lab2/calc/{a}/1')


@lab2.route('/lab2/books/')
def books():
    books = [
    {
        "title": "Война и мир",
        "author": "Лев Толстой",
        "pages": 1225,
        "genre": "Исторический роман",
    },
    {
        "title": "1984",
        "author": "Джордж Оруэлл",
        "pages": 328,
        "genre": "Антиутопия",
    },
    {
        "title": "Мастер и Маргарита",
        "author": "Михаил Булгаков",
        "pages": 448,
        "genre": "Магический реализм",
    },
    {
        "title": "Преступление и наказание",
        "author": "Фёдор Достоевский",
        "pages": 672,
        "genre": "Психологический роман",
    },
    {
        "title": "Убийство в «Восточном экспрессе»",
        "author": "Агата Кристи",
        "pages": 256,
        "genre": "Детектив",
    },
    {
        "title": "Дюна",
        "author": "Фрэнк Герберт",
        "pages": 704,
        "genre": "Научная фантастика",
    },
    {
        "title": "Хоббит, или Туда и обратно",
        "author": "Дж. Р. Р. Толкин",
        "pages": 310,
        "genre": "Фэнтези",
    },
    {
        "title": "Маленький принц",
        "author": "Антуан де Сент-Экзюпери",
        "pages": 96,
        "genre": "Философская сказка",
    },
    {
        "title": "Сияние",
        "author": "Стивен Кинг",
        "pages": 544,
        "genre": "Ужасы",
    },
    {
        "title": "Гордость и предубеждение",
        "author": "Джейн Остин",
        "pages": 416,
        "genre": "Классический роман",
    },
]
    return render_template('lab2/books.html', books = books)


@lab2.route('/lab2/objects/')
def objects():
    obj = [
            {
            "brand": "Toyota",
            "model": "GR Yaris",
            "year": 2020,
            "image": "toyota_gr_yaris.jpg",
        },
        {
            "brand": "Toyota",
            "model": "GR Supra",
            "year": 2019,
            "image": "toyota_gr_supra.jpg",
        },
        {
            "brand": "Toyota",
            "model": "GR86",
            "year": 2021,
            "image": "toyota_gr86.jpg",
        },
        {
            "brand": "Toyota",
            "model": "Land Cruiser 300",
            "year": 2021,
            "image": "toyota_land_cruiser_300.jpg",
        },
        {
            "brand": "Lexus",
            "model": "LFA",
            "year": 2010,
            "image": "lexus_lfa.jpg",
        },
        {
            "brand": "Lexus",
            "model": "LC 500",
            "year": 2017,
            "image": "lexus_lc_500.jpg",
        },
        {
            "brand": "Lexus",
            "model": "IS 500 F",
            "year": 2021,
            "image": "lexus_is_500_f.jpg",
        },
        {
            "brand": "Nissan",
            "model": "GT-R Nismo",
            "year": 2014,
            "image": "nissan_gtr_nismo.jpg",
        },
        {
            "brand": "Nissan",
            "model": "Z350",
            "year": 2022,
            "image": "nissan_z350.jpg",
        },
        {
            "brand": "Nissan",
            "model": "Leaf",
            "year": 2010,
            "image": "nissan_leaf.jpg",
        },
        {
            "brand": "Honda",
            "model": "Civic Type R",
            "year": 2022,
            "image": "honda_civic_type_r.jpg",
        },
        {
            "brand": "Honda",
            "model": "NSX",
            "year": 2016,
            "image": "honda_nsx.jpg",
        },
        {
            "brand": "Honda",
            "model": "S660",
            "year": 2015,
            "image": "honda_s660.jpg",
        },
        {
            "brand": "Mazda",
            "model": "MX-5 Miata",
            "year": 2015,
            "image": "mazda_mx5_miata.jpg",
        },
        {
            "brand": "Mazda",
            "model": "CX-60",
            "year": 2022,
            "image": "mazda_cx60.jpg",
        },
        {
            "brand": "Subaru",
            "model": "BRZ",
            "year": 2021,
            "image": "subaru_brz.jpg",
        },
        {
            "brand": "Subaru",
            "model": "WRX",
            "year": 2021,
            "image": "subaru_wrx.jpg",
        },
        {
            "brand": "Mitsubishi",
            "model": "Lancer Evolution X",
            "year": 2015,
            "image": "mitsubishi_lancer_evo_x.jpg",
        },
        {
            "brand": "Suzuki",
            "model": "Jimny",
            "year": 2018,
            "image": "suzuki_jimny.jpg",
        },
        {
            "brand": "Suzuki",
            "model": "Swift Sport",
            "year": 2017,
            "image": "suzuki_swift_sport.jpg",
        }
    ]
    return render_template('lab2/objects.html', obj = obj)