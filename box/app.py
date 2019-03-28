from sanic import Sanic
from sanic.request import Request
from sanic.response import text

from box.conf import Config, Testing, Development, Production
from box.routes import api_v1
from box.routes.middlewares import set_security_headers

BEFORE_RESPONSE = 'response'
PING = 'ping'


def init_config(env: str = 'default') -> Config:
    mapping = {
        'default': Config,
        'testing': Testing,
        'development': Development,
        'production': Production,
    }
    config = mapping[env](env=env)
    check_env_type(config)

    return config


def check_env_type(config: Config):
    if config.env == 'production' and config.DEBUG:
        raise RuntimeError('You should set DEBUG to false in production')


def init_middleware(app: Sanic) -> None:
    app.register_middleware(set_security_headers, BEFORE_RESPONSE)


def init_blueprints(app: Sanic) -> None:
    app.blueprint(api_v1)


def create_app() -> Sanic:
    app_ = Sanic(__name__)

    app_.config.from_object(init_config())
    init_middleware(app_)
    init_blueprints(app_)

    @app_.route('/')
    def ping(_: Request):
        return text(PING, 200)

    return app_
