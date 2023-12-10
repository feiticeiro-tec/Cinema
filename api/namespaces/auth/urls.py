from . import np_auth
from .resources import AuthResource, AuthRegisterResource

np_auth.add_resource(AuthResource, "/")
np_auth.add_resource(AuthRegisterResource, "/register/")
