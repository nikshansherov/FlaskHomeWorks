from flask import request, render_template, Flask, redirect, url_for
from flask_wtf import CSRFProtect
from werkzeug.security import check_password_hash
from forms import LoginForm, RegistrationForm
from models import User, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)
app.config['SECRET_KEY'] = 'mysecretkey'
csrf = CSRFProtect(app)


@app.route('/home/<name>')
def home(name):
    return render_template('home.html', name=name)


@app.route('/get_out/')
def get_out():
    return render_template('get_out.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            error_msg = 'User alredy exists'
            form.email.errors.append(error_msg)
            return render_template('register.html', form=form)
        new_user = User(firstname=form.firstname.data, lastname=form.lastname.data,
                        email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate():
        password = form.password.data
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, password):
            return redirect(url_for('home', name=user.firstname))
        return redirect(url_for('login'))
    return render_template('login.html', form=form)


# @app.cli.command('init_db')
# def init_db():
#     db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
