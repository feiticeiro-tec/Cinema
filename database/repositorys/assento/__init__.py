from ...models import Assento
from .exceptions import (
    NotFoundAssentoException as NotFound,
    DuplocadoAssentoException as Duplicado,
)
from ... import db


class AssentoRepository:
    NotFoundAssentoException = NotFound
    DuplocadoAssentoException = Duplicado

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
        cls.exists_in_local(fileira, numero, sala_id, raiser=True)
        repo = cls()
        repo.set_local(fileira, numero)
        repo.set_sala_id(sala_id)
        return repo

    def update(self, fileira, numero, is_ativo):
        self.exists_in_local(
            fileira,
            numero,
            self.assento.sala_id,
            id_not_in=[self.assento.id],
            raiser=True,
        )
        self.set_local(fileira, numero)
        self.set_ativo(is_ativo)

    @classmethod
    def exists_in_local(
        cls,
        fileira,
        numero,
        sala_id,
        id_not_in=[],
        raiser=False,
    ):
        assento = (
            db.session.query(Assento.id)
            .filter(
                Assento.fileira == fileira,
                Assento.numero == numero,
                Assento.sala_id == sala_id,
                Assento.id.notin_(id_not_in),
            )
            .first()
        )
        if raiser and assento:
            raise cls.DuplocadoAssentoException()

        if assento:
            return True
        return False

    @classmethod
    def get_all_in_sala_id(cls, sala_id, offset=0, limit=10):
        assentos = (
            db.session.query(Assento)
            .filter(Assento.sala_id == sala_id)
            .offset(offset)
            .limit(limit)
            .all()
        )
        return assentos

    def add(self):
        db.session.add(self.assento)

    @classmethod
    def commit(cls):
        db.session.commit()
