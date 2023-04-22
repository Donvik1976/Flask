from flask import Blueprint, render_template, redirect
from flask_login import login_required
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {
        'title': 'article_1',
        'text': 'article_1_jsfghsshfdS',
        'author': 1
    },
    2: {
        'title': 'article_2',
        'text': 'article_2_jshjfdhjSDHFJH',
        'author': 2
    },
    3: {
        'title': 'article_3',
        'text': 'article_3_jshjfdhjSDHFJH',
        'author': 2
    }
}


@article.route('/')
@login_required
def article_list():
    return render_template(
        'articles/list.html',
        articles=ARTICLES,
    )


@article.route('/<int:pk>')
@login_required
def get_article(pk: int):
    try:
        article_name = ARTICLES[pk]
    except KeyError:
        # raise NotFound(f'User id {pk} not found')
        return redirect('/articles/')
    return render_template(
        'articles/details.html',
        article_name=article_name,
    )
