from flask import Flask, render_template, request, url_for, \
    redirect, make_response

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    email = request.form.get('email')
    if request.cookies.get('log_name'):
        name = request.cookies.get('log_name')
        return redirect(url_for('hello', name=name))
    if request.method == 'POST':
        name = request.form.get('name')
        return redirect(url_for('set_cookies', name=name))
    return render_template('form.html')


@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello(name):
    return render_template('hello.html', name=name)


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/set_cookies/<name>', methods=['GET', 'POST'])
def set_cookies(name):
    res_name = make_response(f'<h1>{name}, для Вашего удобства мы '
                             f'Вас сохранили'
                             f'</h1><br><a href="/home">Перейти на домашнюю страницу</a>')
    res_name.set_cookie('log_name', name)
    return res_name


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    res = make_response("<h1>Вы больше не авторизованы!</h1><br>"
                        "<a href='/'>Перейти на страницу авторизации</a>")
    res.set_cookie("log_name", "", 0)
    return res


if __name__ == '__main__':
    app.run(debug=True)
