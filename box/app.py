from sanic import Sanic
from sanic.request import Request
from sanic.response import text

from box.conf import Config
from box.presentation.middlewares import set_security_headers

BEFORE_RESPONSE = 'response'
PING = 'ping'


def init_config(app: Sanic) -> None:
    app.config.from_object(Config)


def init_middleware(app: Sanic) -> None:
    app.register_middleware(set_security_headers, BEFORE_RESPONSE)


def create_app() -> Sanic:
    app_ = Sanic(__name__)

    init_config(app_)
    init_middleware(app_)

    @app_.route('/')
    def ping(_: Request):
        return text(PING, 200)

    return app_
