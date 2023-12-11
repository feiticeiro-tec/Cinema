from database.repositorys import ColaboradorRepository
from .contratos import Contratos
from .exceptions import Exceptions


class ColaboradorCase:
    Contratos = Contratos
    Exceptions = Exceptions

    def __init__(self, repository: ColaboradorRepository = None):
        if repository is None:
            repository = ColaboradorRepository()
        elif isinstance(repository, ColaboradorRepository):
            repository = ColaboradorRepository()
        self.repository = repository

    @classmethod
    def check_contrato(cls, contrato, tipo_contrato):
        if not isinstance(contrato, tipo_contrato):
            raise cls.Exceptions.ContratoInvalido()

    @classmethod
    def create(cls, contrato: "Contratos.CreateContrato"):
        """Cria um novo colaborador.

        raises: Exceptions.Duplicado, Exceptions.ContratoInvalido"""
        cls.check_contrato(contrato, cls.Contratos.CreateContrato)
        repo: ColaboradorRepository = cls().repository.new(
            usuario_id=contrato.usuario_id,
            cinema_id=contrato.cinema_id,
            is_admin=contrato.is_admin,
        )
        repo.add()
        return cls(repo)

    def commit(self):
        self.repository.commit()
        return self
