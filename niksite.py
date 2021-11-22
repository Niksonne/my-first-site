# -*- coding: utf-8 -*-
from flask import *
import os
# from flask_ngrok import run_with_ngrok '''local tunnel'''
app = Flask(__name__)
# run_with_ngrok(app) '''local tunnel'''

# @app.route('/')
# def index():
#    return "Первая страница"

@app.route('/')
def index():
    user = "Пользователь"
    return render_template('index.html', title='Домашняя страница',
                           username=user)

@app.route('/second/')
def second():
    numbers = [str(i) for i in range(10)]
    return "<BR>".join(numbers)

"""
@app.route('/news')
def news():
    with open("templates/news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    return render_template('news1.html', news=news_list, title = 'Новости')
"""

@app.route('/first_page')
def first():
    name = url_for('static', filename='img/picture.jpg')
    return render_template('picture.html', name=name, title='Первая HTML-страница')

@app.route('/greeting/<username>')
def greeting(username):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, {username}</title>
                  </head>
                  <body>
                    <h1>Привет, {username}!</h1>
                  </body>
                </html>'''

@app.route('/getnumber/<int:number>')
def get_number(number):
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                  </head>
                  <body>
                    <h1>Запрошено число {number}!</h1>
                  </body>
                </html>'''

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return render_template('form.html', title='Регистрация')
    elif request.method == 'POST':
        print(request.form.get('email'))
        print(request.form.get('password'))
        print(request.form.get('file'))
        print(request.form.get('about'))
        print(request.form.get('accept'))
        print(request.form.get('sex'))
        return render_template('form1.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    # app.run()
    #app.run(port=5000, host='127.0.0.1')
