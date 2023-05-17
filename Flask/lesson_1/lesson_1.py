from flask import Flask

app = Flask(__name__)


@app.route('/')   # вместо декоратора можно использовать app.add_url_rule(, viewfunc=page_index)
def page_index():
    return 'главная'


@app.route('/profile/<uid>')
def page_profile(uid):
    return f'профиль пользователя {uid}</h1>'


@app.route('/feed/')
def page_feed():
    return 'лента пользователя'


@app.route('/messages/')
def page_messages():
    return 'сообщения пользователя'


@app.route('/catalog/items/<itemid>')
def page_items(itemid):
    return f'</h1>страница товара {itemid}</h1>'


# проверка получаемого типа из переменной
@app.route('/str/<int:types>')  # с помощью int: превращаем в число
def page_types(types):
    print(types)
    print(type(types))

    return ''


app.run()

