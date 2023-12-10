from flask_restx import fields
from . import np_auth

form_login = np_auth.model(
    "LoginContrato",
    {
        "email": fields.String(required=True),
        "senha": fields.String(required=True),
    },
)
form_register = np_auth.model(
    "AuthRegisterContrato",
    {
        "nome": fields.String(required=True),
        "email": fields.String(required=True),
        "senha": fields.String(required=True),
    },
)

form_confirmar_registro = np_auth.model(
    "ConfirmUsuario",
    {
        "nome": fields.String(required=True),
        "senha": fields.String(required=True),
    },
)
