from flask_restx import Api, Resource, abort, fields
from core.cases.usuario.contratos import Contratos
from core.cases.usuario import UsuarioCase
from flask_pydantic import validate
from ... import api

np_auth = api.namespace("auth", description="Authentication")


def init_app(app):
    api.init_app(app)


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


class AuthResource(Resource):
    @np_auth.expect(form_login)
    @validate()
    def post(self, body: Contratos.LoginContrato):
        """Fazer login"""
        try:
            case = UsuarioCase.login(body)
        except UsuarioCase.Exceptions.ConfirmacaoInvalida:
            abort(401, "Login ou senha incorretos")
        return {"usuario": case.repository.usuario.id}


class AuthRegisterResource(Resource):
    @np_auth.expect(form_register)
    @validate()
    def post(self, body: Contratos.CreateContrato):
        """Cadastrar usuario"""
        try:
            case = UsuarioCase.create(body)
            case.commit()
        except UsuarioCase.Exceptions.UsuarioDuplicado:
            abort(409, "Usuário já cadastrado")
        return {
            "titulo": "Usuário cadastrado com sucesso",
            "message": "Um email de confirmação foi enviado para o seu email",
        }, 201

    @np_auth.expect(form_confirmar_registro)
    @validate()
    def put(self, body: Contratos.ConfirmUsuario):
        """Confirmar cadastro de usuario"""
        try:
            case = UsuarioCase.confirm_account(body)
            case.commit()
        except UsuarioCase.Exceptions.NotFoundUsuarioException:
            abort(400, "Token Invalido")
        return {
            "titulo": "Conta confirmada com sucesso",
            "message": "Agora você pode fazer login",
        }


np_auth.add_resource(AuthResource, "/")
np_auth.add_resource(AuthRegisterResource, "/register/")
