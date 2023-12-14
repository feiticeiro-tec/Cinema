from core.cases import UsuarioCase
from database.repositorys import CinemaRepository, ColaboradorRepository
from core.controllers.cinema import CreateCinemaWithColaboradorController


def test_create(app):
    with app.app_context():
        case = UsuarioCase.create(
            UsuarioCase.Contratos.CreateContrato(
                email="email@host.com",
                nome="nome",
                senha="senha",
            )
        )
        case.commit()
        usuario_id = case.repository.usuario.id

    with app.app_context():
        Contrato = CreateCinemaWithColaboradorController.ExecuteContrato
        controller = CreateCinemaWithColaboradorController()
        controller.execute(
            Contrato(
                cinema=Contrato.Cinema(
                    nome="nome",
                    descricao="descricao",
                    endereco=Contrato.Cinema.Endereco(
                        cep="cep",
                        uf="uf",
                        cidade="cidade",
                        bairro="bairro",
                        rua="rua",
                        numero=2,
                        complemento="complemento",
                        referencia="referencia",
                    ),
                ),
                usuario_id=usuario_id,
            )
        )
    with app.app_context():
        cinema = CinemaRepository.get_all()[0]
        colaborador = ColaboradorRepository.get_by_usuario_id(usuario_id)
        assert colaborador.is_admin is True
        assert colaborador.cinema_id == cinema.id
