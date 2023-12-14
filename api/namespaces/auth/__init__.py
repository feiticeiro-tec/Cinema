from importlib import import_module
from ... import api

np_auth = api.namespace("auth", description="Authentication")
import_module(".urls", package=__name__)
