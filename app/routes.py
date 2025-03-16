from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    username = "Timur"
    return render_template("index.html", username=username)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Вход запрошен для {form.username.data}, c паролем {form.password.data}')
        return redirect(url_for('login'))

    return render_template("login.html", title='Вход', form=form)