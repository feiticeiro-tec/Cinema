from database.models import colaborador
from ...models import Colaborador
from .exceptions import NotFoundColaboradorException, DuplicadoColaboradorException
from ... import db


class ColaboradorRepository:
    NotFoundColaboradorException = NotFoundColaboradorException
    DuplicadoColaboradorException = DuplicadoColaboradorException

    def __init__(self, colaborador: Colaborador = None):
        if not colaborador:
            colaborador = Colaborador()
        self.colaborador = colaborador

    @classmethod
    def use_by_id(cls, id):
        return cls(cls.get_by_id(id))

    @classmethod
    def get_by_id(cls, id) -> Colaborador:
        colaborador = Colaborador.query.filter_by(id=id).first()
        if not colaborador:
            raise cls.NotFoundColaboradorException()
        return colaborador

    @classmethod
    def get_by_usuario_id(cls, usuario_id) -> Colaborador:
        colaborador = Colaborador.query.filter_by(usuario_id=usuario_id).first()
        if not colaborador:
            raise cls.NotFoundColaboradorException()
        return colaborador

    @classmethod
    def use_by_usuario_id(cls, usuario_id):
        return cls(cls.get_by_usuario_id(usuario_id))

    @classmethod
    def usuario_is_admin(cls, usuario_id):
        return (
            db.session.query(Colaborador.is_admin)
            .filter_by(usuario_id=usuario_id)
            .scalar()
        )

    @classmethod
    def new(cls, usuario_id, cinema_id, is_admin=False):
        if cls.is_usuario_exist_on_cinema(
            usuario_id=usuario_id,
            cinema_id=cinema_id,
        ):
            raise cls.DuplicadoColaboradorException()
        return cls(
            Colaborador(
                usuario_id=usuario_id,
                cinema_id=cinema_id,
                is_admin=is_admin,
            )
        )

    @classmethod
    def is_usuario_exist_on_cinema(cls, usuario_id, cinema_id):
        colaborador = (
            db.session.query(Colaborador.id)
            .filter(
                Colaborador.usuario_id == usuario_id,
                Colaborador.cinema_id == cinema_id,
            )
            .first()
        )
        if colaborador:
            return True
        return False

    def add(self):
        db.session.add(self.colaborador)

    def commit(self):
        db.session.commit()
