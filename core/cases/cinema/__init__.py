from database.repositorys import CinemaRepository
from .contratos import Contratos
from .excpetions import Exceptions


class CinemaCase:
    Contratos = Contratos
    Exceptions = Exceptions

    def __init__(self, repository: CinemaRepository = None):
        if repository is None:
            repository = CinemaRepository()
        elif not isinstance(repository, CinemaRepository):
            repository = CinemaRepository(repository)
        self.repository = repository

    @classmethod
    def check_contrato(cls, contrato, tipo_contrato):
        if not isinstance(contrato, tipo_contrato):
            raise cls.Exceptions.ContratoInvalido()

    def commit(self):
        self.repository.commit()

    @classmethod
    def create(cls, contrato: "Contratos.CreateContrato"):
        cls.check_contrato(contrato, cls.Contratos.CreateContrato)
        repo = cls().repository.new(
            nome=contrato.nome,
            descricao=contrato.descricao,
            endereco=contrato.endereco,
        )
        repo.add()
        return cls(repo)
