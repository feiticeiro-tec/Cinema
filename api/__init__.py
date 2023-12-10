from flask_restx import Api
from importlib import import_module
from flask_jwt_extended import JWTManager

api = Api()
jm = JWTManager()


def init_app(app):
    api.init_app(app)
    jm.init_app(app)
    import_module(".namespaces", package=__name__)
