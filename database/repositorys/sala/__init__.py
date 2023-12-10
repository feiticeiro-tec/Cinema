from ...models import Sala
from ... import db
from .exceptions import (
    NotFoundSalaException as NotFound,
)


class SalaRepository:
    NotFoundSalaException = NotFound

    def __init__(self, sala: Sala = None):
        if not sala:
            sala = Sala()
        self.sala = sala

    @classmethod
    def get_by_id(cls, id):
        sala = Sala.query.filter(Sala.id == id).first()
        if not sala:
            raise cls.NotFoundSalaException()
        return sala
