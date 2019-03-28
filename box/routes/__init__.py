from sanic import Blueprint

from .auth import auth_bp
from .user_info import user_bp
from .article import article_bp


api_v1 = Blueprint.group(
    auth_bp,
    user_bp,
    article_bp,
    url_prefix='/api/v1'
)
