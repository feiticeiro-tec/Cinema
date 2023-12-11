from flask_restx import Api
from importlib import import_module
from flask_jwt_extended import JWTManager
from flask_cors import CORS

api = Api()
jm = JWTManager()
cors = CORS()


def init_app(app):
    api.init_app(app)
    jm.init_app(app)
    cors.init_app(app)
    import_module(".namespaces", package=__name__)
