from database.repositorys.usuario import UsuarioRepository, Usuario
from .contratos import (
    UsuarioCreate,
    UsuarioUpdateInfos,
)
from .exceptions import ContratoInvalido, ConfirmacaoInvalida


class UsuarioCase:
    ContratoInvalido = ContratoInvalido
    ConfirmacaoInvalida = ConfirmacaoInvalida

    class Contratos:
        CreateContrato = UsuarioCreate
        UsuarioUpdateInfos = UsuarioUpdateInfos

    def __init__(self, repository: UsuarioRepository):
        if isinstance(repository, Usuario):
            repository = UsuarioRepository(repository)
        self.repository = repository

    @classmethod
    def check_contrato(cls, contrato, tipo_contrato):
        if not isinstance(contrato, tipo_contrato):
            raise cls.ContratoInvalido()

    @classmethod
    def create(cls, contrato: "Contratos.CreateContrato"):
        cls.check_contrato(contrato, cls.Contratos.CreateContrato)
        repo = UsuarioRepository.new(
            nome=contrato.nome,
            email=contrato.email,
            senha=contrato.senha,
        )
        repo.add()

        return cls(repo)

    def commit(self):
        self.repository.commit()
        return self
