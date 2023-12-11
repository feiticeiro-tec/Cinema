import pytest
from database.repositorys import CinemaRepository
from database.repositorys import UsuarioRepository
from core.cases.colaborador import ColaboradorCase
from database.repositorys.colaborador import ColaboradorRepository


def test_create(app):
    with app.app_context():
        repo = UsuarioRepository()
        repo.set_credencial(
            email="email@host.com",
            senha="senha",
        )
        repo.set_nome("nome")
        repo.add()
        repo.flush()
        usuario_id = repo.usuario.id

        repo = CinemaRepository()
        repo.set_infos(
            nome="nome",
            descricao="descricao",
        )
        repo.set_endereco(
            CinemaRepository.Endereco(
                cep="cep",
                uf="uf",
                cidade="cidade",
                bairro="bairro",
                rua="rua",
                numero=2,
                complemento="complemento",
                referencia="referencia",
            )
        )
        repo.add()
        repo.commit()
        cinema_id = repo.cinema.id

    with app.app_context():
        case = ColaboradorCase.create(
            ColaboradorCase.Contratos.CreateContrato(
                usuario_id=usuario_id,
                cinema_id=cinema_id,
            )
        )
        case.commit()

    with app.app_context():
        colaborador = ColaboradorRepository.get_by_usuario_id(usuario_id)
        assert colaborador.is_admin is False
        assert colaborador.cinema_id == cinema_id


def test_create_duplicado(app):
    with app.app_context():
        repo = UsuarioRepository()
        repo.set_credencial(
            email="email@host.com",
            senha="senha",
        )
        repo.set_nome("nome")
        repo.add()
        repo.flush()
        usuario_id = repo.usuario.id

        repo = CinemaRepository()
        repo.set_infos(
            nome="nome",
            descricao="descricao",
        )
        repo.set_endereco(
            CinemaRepository.Endereco(
                cep="cep",
                uf="uf",
                cidade="cidade",
                bairro="bairro",
                rua="rua",
                numero=2,
                complemento="complemento",
                referencia="referencia",
            )
        )
        repo.add()
        repo.commit()
        cinema_id = repo.cinema.id

        case = ColaboradorCase.create(
            ColaboradorCase.Contratos.CreateContrato(
                usuario_id=usuario_id,
                cinema_id=cinema_id,
            )
        )
        case.commit()

    with app.app_context():
        with pytest.raises(ColaboradorCase.Exceptions.Duplicado):
            case = ColaboradorCase.create(
                ColaboradorCase.Contratos.CreateContrato(
                    usuario_id=usuario_id,
                    cinema_id=cinema_id,
                )
            )
            case.commit()
