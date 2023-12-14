from flask_restx import fields
from . import np_auth

form_login = np_auth.model(
    "LoginContrato",
    {
        "email": fields.String(required=True, example="teste@host.com"),
        "senha": fields.String(required=True, example="senha123"),
    },
)
form_register = np_auth.model(
    "AuthRegisterContrato",
    {
        "nome": fields.String(required=True, example="usuario_teste"),
        "email": fields.String(required=True, example="teste@host.com"),
        "senha": fields.String(required=True, example="senha123"),
    },
)

form_confirmar_registro = np_auth.model(
    "ConfirmUsuario",
    {
        "token": fields.String(required=True),
        "senha": fields.String(required=True, example="senha123"),
    },
)
