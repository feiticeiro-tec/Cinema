from ...models import Assento
from .exceptions import NotFoundAssentoException as NotFound
from ... import db


class AssentoRepository:
    NotFoundAssentoException = NotFound

    def __init__(self, assento: Assento = None):
        if not assento:
            assento = Assento()
        self.assento = assento

    @classmethod
    def get_by_id(cls, id):
        assento = Assento.query.filter(Assento.id == id).first()
        if not assento:
            raise cls.NotFoundAssentoException()
        return assento

    @classmethod
    def use_by_id(cls, id):
        return cls(cls.get_by_id(id))

    def set_local(self, fileira, numero):
        self.assento.fileira = fileira
        self.assento.numero = numero

    def set_ativo(self, is_ativo):
        self.assento.is_ativo = is_ativo

    def set_sala_id(self, sala_id):
        self.assento.sala_id = sala_id

    @classmethod
    def new(cls, fileira, numero, sala_id):
        repo = cls()
        repo.set_local(fileira, numero)
        repo.set_sala_id(sala_id)
        return repo

    def update(self, fileira, numero, is_ativo):
        self.set_local(fileira, numero)
        self.set_ativo(is_ativo)

    def add(self):
        db.session.add(self.assento)

    @classmethod
    def commit(cls):
        db.session.commit()
