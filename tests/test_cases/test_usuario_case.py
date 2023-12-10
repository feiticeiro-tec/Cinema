from database.cases.usuario import UsuarioCase, UsuarioRepository
import pytest


def test_create(app):
    with app.app_context():
        contrato = UsuarioCase.Contratos.CreateContrato(
            nome="teste",
            email="email",
            senha="senha",
        )
        case = UsuarioCase.create(contrato)
        case.commit()
        usuario_id = case.repository.usuario.id

    with app.app_context():
        usuario = UsuarioRepository.get_by_id(usuario_id)
        assert usuario.nome == "teste"
        assert usuario.email == "email"
        assert usuario.senha != "senha"
        assert not usuario.is_ativo


def test_create_duplicado(app):
    with app.app_context():
        contrato = UsuarioCase.Contratos.CreateContrato(
            nome="teste",
            email="email",
            senha="senha",
        )
        case = UsuarioCase.create(contrato)
        case.commit()

    with app.app_context():
        with pytest.raises(UsuarioCase.Exceptions.UsuarioDuplicado):
            case = UsuarioCase.create(contrato)


def test_check_contrato():
    with pytest.raises(UsuarioCase.Exceptions.ContratoInvalido):
        UsuarioCase.check_contrato({}, str)


def test_login_valido(app):
    with app.app_context():
        contrato = UsuarioCase.Contratos.CreateContrato(
            nome="teste",
            email="email",
            senha="senha",
        )
        case = UsuarioCase.create(contrato)
        case.repository.set_is_ativo(True)
        case.commit()

    with app.app_context():
        contrato = UsuarioCase.Contratos.LoginContrato(
            email="email",
            senha="senha",
        )
        case = UsuarioCase.login(contrato)
        assert case


def test_login_inativo(app):
    with app.app_context():
        contrato = UsuarioCase.Contratos.CreateContrato(
            nome="teste",
            email="email",
            senha="senha",
        )
        case = UsuarioCase.create(contrato)
        case.commit()

    with app.app_context():
        contrato = UsuarioCase.Contratos.LoginContrato(
            email="email",
            senha="senha",
        )
        with pytest.raises(UsuarioCase.Exceptions.UsuarioInativado):
            UsuarioCase.login(contrato)


def test_login_senha_invalida(app):
    with app.app_context():
        contrato = UsuarioCase.Contratos.CreateContrato(
            nome="teste",
            email="email",
            senha="senha",
        )
        case = UsuarioCase.create(contrato)
        case.repository.set_is_ativo(True)
        case.commit()

    with app.app_context():
        contrato = UsuarioCase.Contratos.LoginContrato(
            email="email",
            senha="senha_errada",
        )
        with pytest.raises(UsuarioCase.Exceptions.ConfirmacaoInvalida):
            UsuarioCase.login(contrato)


def test_login_email_invalida(app):
    with app.app_context():
        contrato = UsuarioCase.Contratos.CreateContrato(
            nome="teste",
            email="email",
            senha="senha",
        )
        case = UsuarioCase.create(contrato)
        case.commit()

    with app.app_context():
        contrato = UsuarioCase.Contratos.LoginContrato(
            email="email_askjd",
            senha="senha",
        )
        with pytest.raises(UsuarioCase.Exceptions.ConfirmacaoInvalida):
            UsuarioCase.login(contrato)


def test_confirm_account(app):
    with app.app_context():
        contrato = UsuarioCase.Contratos.CreateContrato(
            nome="teste",
            email="email",
            senha="senha",
        )
        case = UsuarioCase.create(contrato)
        case.commit()

    with app.app_context():
        usuario = UsuarioRepository.get_by_email(email="email")
        assert not usuario.is_ativo
        contrato = UsuarioCase.Contratos.ConfirmUsuario(
            token=usuario.id,
            senha="senha",
        )
        case = UsuarioCase.confirm_account(contrato)
        assert case.repository.usuario.is_ativo
