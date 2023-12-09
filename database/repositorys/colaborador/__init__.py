from ...models import Colaborador
from .exceptions import NotFoundColaboradorException


class ColaboradorRepository:
    NotFoundColaboradorException = NotFoundColaboradorException

    def __init__(self, colaborador: Colaborador = None):
        if not colaborador:
            colaborador = Colaborador()
        self.colaborador = colaborador

    @classmethod
    def use_by_id(cls, id):
        return cls(cls.get_by_id(id))

    @classmethod
    def get_by_id(cls, id):
        colaborador = Colaborador.query.filter_by(id=id).first()
        if not colaborador:
            raise cls.NotFoundColaboradorException()
        return colaborador
    