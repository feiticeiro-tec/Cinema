from core.cases.cinema import CinemaCase, CinemaRepository


def test_create(app):
    with app.app_context():
        case = CinemaCase.create(
            CinemaCase.Contratos.CreateContrato(
                nome="nome",
                descricao="descricao",
                endereco=CinemaCase.Contratos.CreateContrato.Endereco(
                    cep="cep",
                    uf="uf",
                    cidade="cidade",
                    bairro="bairro",
                    rua="rua",
                    numero=2,
                    complemento="complemento",
                    referencia="referencia",
                ),
            )
        )
        case.commit()
        cinema_id = case.repository.cinema.id

    with app.app_context():
        cinema = CinemaRepository.get_by_id(cinema_id)
        assert cinema.nome == "nome"
        assert cinema.descricao == "descricao"
        assert cinema.cep == "cep"
        assert cinema.uf == "uf"
        assert cinema.cidade == "cidade"
        assert cinema.bairro == "bairro"
        assert cinema.rua == "rua"
        assert cinema.numero == 2
        assert cinema.complemento == "complemento"
        assert cinema.referencia == "referencia"
