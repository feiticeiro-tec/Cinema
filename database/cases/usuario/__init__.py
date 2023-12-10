from database.repositorys.usuario import UsuarioRepository, Usuario
from .contratos import Contratos
from .exceptions import ContratoInvalido, ConfirmacaoInvalida


class UsuarioCase:
    ContratoInvalido = ContratoInvalido
    ConfirmacaoInvalida = ConfirmacaoInvalida
    Contratos = Contratos
    UsuarioDuplicado = UsuarioRepository.DuplicateEmailUsuarioException

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

    @classmethod
    def login(cls, contrato: "Contratos.LoginContrato"):
        cls.check_contrato(contrato, cls.Contratos.LoginContrato)
        try:
            usuario = UsuarioRepository.get_by_email(
                email=contrato.email,
            )
        except UsuarioRepository.NotFoundUsuarioException:
            raise cls.ConfirmacaoInvalida()
        if not contrato.check_login(usuario.senha):
            raise cls.ConfirmacaoInvalida()
        return cls(usuario)
