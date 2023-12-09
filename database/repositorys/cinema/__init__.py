from ...models import Cinema
from .exceptions import NotFoundCinemaException
from .intefaces import Endereco
from database import db


class CinemaRepository:
    NotFoundCinemaException = NotFoundCinemaException
    Endereco = Endereco

    def __init__(self, cinema: Cinema = None):
        if not cinema:
            cinema = Cinema()
        self.cinema = cinema

    @classmethod
    def use_by_id(cls, id):
        return cls(cls.get_by_id(id))

    def set_endereco(self, endereco: "Endereco"):
        self.cinema.cep = endereco.cep
        self.cinema.uf = endereco.uf
        self.cinema.cidade = endereco.cidade
        self.cinema.bairro = endereco.bairro
        self.cinema.rua = endereco.rua
        self.cinema.numero = endereco.numero
        self.cinema.complemento = endereco.complemento
        self.cinema.referencia = endereco.referencia

    def set_infos(self, nome: str, descricao: str):
        self.cinema.nome = nome
        self.cinema.descricao = descricao

    @classmethod
    def get_by_id(cls, id):
        cinema = Cinema.query.filter_by(id=id).first()
        if not cinema:
            raise cls.NotFoundCinemaException()
        return cinema

    @classmethod
    def new(cls, nome: str, descricao: str, endereco: "Endereco"):
        repo = cls()
        repo.set_infos(nome, descricao)
        repo.set_endereco(endereco)
        return repo

    @classmethod
    def get_all(cls, offset: int = 0, limit: int = 10):
        cinemas = Cinema.query.offset(offset).limit(limit).all()
        return cinemas

    def add(self):
        db.session.add(self.cinema)

    @classmethod
    def commit(cls):
        db.session.commit()
