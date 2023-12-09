from ...models import Usuario
from .excpetions import NotFoundUsuarioException
from database import db


class UsuarioRepository:
    def __init__(self, usuario: Usuario = None):
        if not usuario:
            usuario = Usuario()
        self.usuario = usuario

    @classmethod
    def use_by_id(cls, id):
        return cls(cls.get_by_id(id))

    @classmethod
    def get_by_id(self, id):
        usuario = Usuario.query.filter_by(id=id).first()
        if not usuario:
            raise NotFoundUsuarioException()
        return usuario

    def set_credencial(self, email, senha):
        self.usuario.email = email
        self.usuario.senha = senha

    def add(self):
        db.session.add(self.usuario)

    def commit(self):
        db.session.commit()
