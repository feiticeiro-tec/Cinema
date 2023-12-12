from . import np_cinemas
from flask_restx import fields

endereco = np_cinemas.model(
    "CreateCinemaEndereco",
    {
        "cep": fields.String(
            required=True,
            description="CEP do cinema",
        ),
        "uf": fields.String(
            required=True,
            description="UF do cinema",
        ),
        "cidade": fields.String(
            required=True,
            description="Cidade do cinema",
        ),
        "bairro": fields.String(
            required=True,
            description="Bairro do cinema",
        ),
        "rua": fields.String(
            required=True,
            description="Rua do cinema",
        ),
        "numero": fields.Integer(
            required=True,
            description="Número do cinema",
        ),
        "complemento": fields.String(
            required=False, description="Complemento do cinema"
        ),
        "referencia": fields.String(
            required=False,
            description="Referência do cinema",
        ),
    },
)

form_create_cinema = np_cinemas.model(
    "CreateCinema",
    {
        "nome": fields.String(
            required=True,
            description="Nome do cinema",
        ),
        "descricao": fields.String(
            required=False,
            description="Descrição do cinema",
        ),
        "endereco": fields.Nested(endereco, required=True),
    },
)
