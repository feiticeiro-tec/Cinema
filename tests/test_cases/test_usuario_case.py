from database.cases.usuario import UsuarioCase, UsuarioRepository, Usuario


def test_create(app):
    with app.app_context():
        contrato = UsuarioCase.CreateContrato(
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
