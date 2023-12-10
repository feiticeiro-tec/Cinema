from database.repositorys.usuario import UsuarioRepository, Usuario
from .contratos import UsuarioCreateContrato
from .exceptions import ContratoInvalido


class UsuarioCase:
    ContratoInvalido = ContratoInvalido
    CreateContrato = UsuarioCreateContrato

    def __init__(self, repository: UsuarioRepository):
        if isinstance(repository, Usuario):
            repository = UsuarioRepository(repository)
        self.repository = repository

    @classmethod
    def check_contrato(cls, contrato, tipo_contrato):
        if not isinstance(contrato, tipo_contrato):
            raise cls.ContratoInvalido()

    @classmethod
    def create(cls, contrato: "CreateContrato"):
        cls.check_contrato(contrato, cls.CreateContrato)
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
