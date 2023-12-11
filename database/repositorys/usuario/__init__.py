from ...models import Usuario
from .excpetions import (
    NotFoundUsuarioException,
    UsuarioDuplicado,
)
from ... import db


class UsuarioRepository:
    NotFoundUsuarioException = NotFoundUsuarioException
    UsuarioDuplicado = UsuarioDuplicado

    def __init__(self, usuario: Usuario = None):
        if not usuario:
            usuario = Usuario()
        self.usuario = usuario

    @classmethod
    def use_by_id(cls, id: str):
        """Pegar um usuario existente.

        raises: NotFoundUsuarioException
        """
        return cls(cls.get_by_id(id))

    @classmethod
    def use_by_email(cls, email: str):
        return cls(cls.get_by_email(email))

    @classmethod
    def get_by_id(cls, id: str) -> Usuario:
        """Pegar um usuario existente.

        raises: NotFoundUsuarioException
        """
        usuario = Usuario.query.filter_by(id=id).first()
        if not usuario:
            raise cls.NotFoundUsuarioException()
        return usuario

    @classmethod
    def get_all(cls, offset: int, limit: int):
        return Usuario.query.offset(offset).limit(limit).all()

    @classmethod
    def get_by_email(cls, email: str) -> Usuario:
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

    @classmethod
    def exists_email(self, email: str, id_not_in=[], raiser=False):
        usuario = (
            db.session.query(Usuario.id)
            .filter(Usuario.email == email, Usuario.id.notin_(id_not_in))
            .first()
        )
        if raiser and usuario:
            raise self.UsuarioDuplicado()
        return usuario is not None

    @classmethod
    def new(cls, nome: str, email: str, senha: str):
        cls.exists_email(email, raiser=True)
        repo = cls()
        repo.set_credencial(email, senha)
        repo.set_nome(nome)
        return repo

    def update(self, nome: str, email: str, senha: str):
        self.exists_email(email, raiser=True, id_not_in=[self.usuario.id])
        self.set_nome(nome)
        self.set_credencial(email, senha)

    def add(self):
        db.session.add(self.usuario)

    def commit(self):
        db.session.commit()
