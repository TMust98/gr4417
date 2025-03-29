from app import app
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.models import User


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/second")
@login_required
def second():
    text = f"Пользователь {current_user.username}"
    return render_template("second.html", text=text)


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Успешная регистрация!')
        return redirect(url_for("login"))
    return render_template("register.html", form=form, title='Регистрация')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Неправильный логин или пароль!')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page:
            next_page = url_for('index')
        flash('Успешный вход в систему!')
        return redirect(next_page)
    return render_template("login.html", title='Вход', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash("Успешный выход из системы!")
    return redirect(url_for('index'))