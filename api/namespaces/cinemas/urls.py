from . import np_cinemas
from .resources import CinemasResource, CinemasTargetResource

np_cinemas.add_resource(CinemasResource, "/", endpoint="cinemas")
np_cinemas.add_resource(
    CinemasTargetResource,
    "/<uuid:id>/",
    endpoint="cinemas-target",
)
