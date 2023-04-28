import click
from werkzeug.security import generate_password_hash

from blog.extensions import db


# @click.command('init-db')
# def init_db():
#     from wsgi import app
#     from blog.models import User
#
#     db.create_all()


@click.command('create-init-user')
def create_init_user():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(username='vik2', email='vic2@vic.com', password=generate_password_hash('123'),
                 is_admin=False)
        )
        db.session.commit()


@click.command('create-admin')
def create_admin():
    from blog.models import User
    from wsgi import app

    with app.app_context():
        db.session.add(
            User(username='admin_vik', email='admin@vik.com', password=generate_password_hash('123'),
                 is_admin=True)
        )
        db.session.commit()
