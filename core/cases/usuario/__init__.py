from database.repositorys.usuario import UsuarioRepository, Usuario
from .contratos import Contratos
from .exceptions import Exceptions


class UsuarioCase:
    Contratos = Contratos
    Exceptions = Exceptions

    def __init__(self, repository: UsuarioRepository = None):
        if repository is None:
            repository = UsuarioRepository()
        elif isinstance(repository, Usuario):
            repository = UsuarioRepository(repository)
        self.repository = repository

    @classmethod
    def check_contrato(cls, contrato, tipo_contrato):
        if not isinstance(contrato, tipo_contrato):
            raise cls.Exceptions.ContratoInvalido()

    @classmethod
    def create(cls, contrato: "Contratos.CreateContrato"):
        cls.check_contrato(contrato, cls.Contratos.CreateContrato)
        repo = cls().repository.new(
            nome=contrato.nome,
            email=contrato.email,
            senha=contrato.senha,
        )
        repo.set_is_ativo(False)
        repo.add()

        return cls(repo)

    def commit(self):
        self.repository.commit()
        return self

    @classmethod
    def login(cls, contrato: "Contratos.LoginContrato"):
        cls.check_contrato(contrato, cls.Contratos.LoginContrato)
        try:
            usuario = cls().repository.get_by_email(
                email=contrato.email,
            )
        except cls().repository.NotFoundUsuarioException:
            raise cls.Exceptions.ConfirmacaoInvalida()
        if not usuario.is_ativo:
            raise cls.Exceptions.UsuarioInativado()
        if not contrato.check_login(usuario.senha):
            raise cls.Exceptions.ConfirmacaoInvalida()
        return cls(usuario)

    @classmethod
    def confirm_account(cls, contrato: "Contratos.ConfirmUsuario"):
        """confirmar conta de usuario

        raises: NotFoundUsuarioException

        """
        cls.check_contrato(contrato, cls.Contratos.ConfirmUsuario)
        usuario = cls().repository.use_by_id(id=contrato.token)
        usuario.set_is_ativo(True)
        return cls(usuario)
