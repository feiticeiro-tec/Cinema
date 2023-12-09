from ...models import Usuario
from .excpetions import NotFoundUsuarioException
from database import db


class UsuarioRepository:
    def __init__(self, usuario: Usuario = None):
        if not usuario:
            usuario = Usuario()
        self.usuario = usuario

    @classmethod
    def use_by_id(cls, id: str):
        return cls(cls.get_by_id(id))

    @classmethod
    def use_by_email(cls, email: str):
        return cls(cls.get_by_email(email))

    @classmethod
    def get_by_id(self, id: str):
        usuario = Usuario.query.filter_by(id=id).first()
        if not usuario:
            raise NotFoundUsuarioException()
        return usuario

    @classmethod
    def get_all(cls, offset: int, limit: int):
        return Usuario.query.offset(offset).limit(limit).all()

    @classmethod
    def get_by_email(cls, email: str):
        usuario = Usuario.query.filter_by(email=email).first()
        if not usuario:
            raise NotFoundUsuarioException()
        return usuario

    def set_credencial(self, email: str, senha: str):
        self.usuario.email = email
        self.usuario.senha = senha

    def set_nome(self, nome: str):
        self.usuario.nome = nome

    def set_is_ativo(self, is_ativo: bool):
        self.usuario.is_ativo = is_ativo

    def add(self):
        db.session.add(self.usuario)

    def commit(self):
        db.session.commit()
