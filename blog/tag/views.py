from flask import Blueprint, render_template

from blog.models import Tag
from werkzeug.exceptions import NotFound


tag = Blueprint('tag', __name__, url_prefix='/tags', static_folder='../static')


@tag.route('/')
def tag_list():
    tags = Tag.query.all()
    return render_template(
        'tags/list.html',
        tags=tags,
    )


@tag.route('/<int:tag_id>/', methods=['GET'])
def tag_detail(tag_id):
    _tag: Tag = Tag.query.filter_by(id=tag_id).one_or_none()

    if _tag is None:
        raise NotFound
    return render_template(
        'tags/profile.html',
        tag=_tag,
    )