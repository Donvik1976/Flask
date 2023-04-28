from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import logout_user, login_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from blog.forms.user import UserLoginForm
from blog.extensions import db
from blog.models import User

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserLoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user or not check_password_hash(user.password, form.password.data):
            flash('Check your login details')
            return render_template('auth/login.html', form=form)

        login_user(user)
        return redirect(url_for('user.profile', pk=user.id))

    return render_template(
        'auth/login.html',
        form=form,
    )


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))
