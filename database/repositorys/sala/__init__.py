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

    @classmethod
    def use_by_id(cls, id):
        return cls(cls.get_by_id(id))

    def set_infos(self, nome, descricao):
        self.sala.nome = nome
        self.sala.descricao = descricao

    def set_cinema_id(self, cinema_id):
        self.sala.cinema_id = cinema_id

    @classmethod
    def new(cls, nome, descricao, cinema_id):
        repo = cls()
        repo.set_infos(nome, descricao)
        repo.set_cinema_id(cinema_id)
        return repo

    def add(self):
        db.session.add(self.sala)

    def commit(self):
        db.session.commit()
