from ...models import Usuario
from .excpetions import NotFoundUsuarioException


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
