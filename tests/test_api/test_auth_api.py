from core.cases.usuario import UsuarioCase


def test_criacao_de_usuario(app):
    with app.test_client() as client:
        response = client.post(
            "/auth/register/",
            json={
                "nome": "teste",
                "email": "email@gmail.com",
                "senha": "123456",
            },
        )
        assert response.status_code == 201
        assert response.json == {
            "titulo": "Usuário cadastrado com sucesso",
            "message": "Um email de confirmação foi enviado para o seu email",
        }


def test_confirmacao_de_conta(app):
    with app.test_client() as client:
        case = UsuarioCase.create(
            UsuarioCase.Contratos.CreateContrato(
                nome="teste",
                email="email@gmail.com",
                senha="123456",
            )
        )
        case.commit()
        token = case.repository.usuario.id

    with app.test_client() as client:
        response = client.put(
            "/auth/register/",
            json={
                "token": token,
                "senha": "123456",
            },
        )
        assert response.status_code == 200
        assert response.json == {
            "titulo": "Conta confirmada com sucesso",
            "message": "Agora você pode fazer login",
        }


def test_login(app):
    with app.test_client() as client:
        case = UsuarioCase.create(
            UsuarioCase.Contratos.CreateContrato(
                nome="teste",
                email="email@gmail.com",
                senha="123456",
            )
        )
        case.commit()
        usuario_id = case.repository.usuario.id
        case.confirm_account(
            UsuarioCase.Contratos.ConfirmUsuario(
                token=usuario_id,
                senha="123456",
            )
        )

    with app.test_client() as client:
        response = client.post(
            "/auth/",
            json={
                "email": "email@gmail.com",
                "senha": "123456",
            },
        )
        assert response.status_code == 200
        assert response.json["access_token"]
