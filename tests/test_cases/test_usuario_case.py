from database.cases.usuario import UsuarioCase, UsuarioRepository, Usuario
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


def test_check_contrato():
    with pytest.raises(UsuarioCase.ContratoInvalido):
        UsuarioCase.check_contrato({}, str)


def test_login_valido(app):
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
        case = UsuarioCase.login(contrato)
        assert case


def test_login_senha_invalida(app):
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
            senha="senha_errada",
        )
        with pytest.raises(UsuarioCase.ConfirmacaoInvalida):
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
        with pytest.raises(UsuarioCase.ConfirmacaoInvalida):
            UsuarioCase.login(contrato)
