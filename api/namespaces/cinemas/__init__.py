from importlib import import_module
from ... import api

np_cinemas = api.namespace("cinemas", description="Cinemas")
import_module(".urls", package=__name__)
