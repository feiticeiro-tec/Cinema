from database.repositorys import CinemaRepository
from core.cases import CinemaCase


def test_criacao_de_cinema(usuario_login):
    with usuario_login.test_client() as client:
        response = client.post(
            "/cinemas/",
            headers={"Authorization": usuario_login.access_token},
            json={
                "nome": "Cinema 1",
                "descricao": "Cinema 1",
                "endereco": {
                    "cep": "00000000",
                    "uf": "UF",
                    "cidade": "Cidade",
                    "bairro": "Bairro",
                    "rua": "Rua",
                    "numero": 0,
                    "complemento": "Complemento",
                    "referencia": "Referencia",
                },
            },
        )
        assert response.status_code == 201
        assert response.json["data"]["id"]
        assert response.json["_self"]

    with usuario_login.app_context():
        cinema = CinemaRepository.get_by_id(response.json["data"]["id"])
        assert cinema.nome == "Cinema 1"
        assert cinema.descricao == "Cinema 1"
        assert cinema.cep == "00000000"
        assert cinema.uf == "UF"
        assert cinema.cidade == "Cidade"
        assert cinema.bairro == "Bairro"
        assert cinema.rua == "Rua"
        assert cinema.numero == 0
        assert cinema.complemento == "Complemento"
        assert cinema.referencia == "Referencia"


def test_get_cinemas(app):
    with app.app_context():
        for i in range(4):
            cinema = CinemaCase.create(
                CinemaCase.Contratos.CreateContrato(
                    nome=f"Cinema {i}",
                    descricao=f"Cinema {i}",
                    endereco=CinemaCase.Contratos.CreateContrato.Endereco(
                        cep="00000000",
                        uf="UF",
                        cidade="Cidade",
                        bairro="Bairro",
                        rua="Rua",
                        numero=0,
                        complemento="Complemento",
                        referencia="Referencia",
                    ),
                )
            )
        cinema.commit()

    with app.test_client() as client:
        response = client.get(
            "/cinemas/",
        )
        assert response.status_code == 200
        assert len(response.json["data"]) == 4
        for i in range(4):
            assert response.json["data"][i]["nome"] == f"Cinema {i}"


def test_get_cinema_by_id(app):
    with app.app_context():
        cinema = CinemaCase.create(
            CinemaCase.Contratos.CreateContrato(
                nome="Cinema",
                descricao="Cinema",
                endereco=CinemaCase.Contratos.CreateContrato.Endereco(
                    cep="00000000",
                    uf="UF",
                    cidade="Cidade",
                    bairro="Bairro",
                    rua="Rua",
                    numero=0,
                    complemento="Complemento",
                    referencia="Referencia",
                ),
            )
        )
        cinema.commit()
        cinema_id = cinema.repository.cinema.id
    with app.test_client() as client:
        response = client.get(f"/cinemas/{cinema_id}/")
        assert response.status_code == 200
        assert response.json["data"]["nome"] == "Cinema"
