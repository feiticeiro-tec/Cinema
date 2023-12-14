from flask_restx import Resource, abort
from flask_pydantic import validate
from core.cases.usuario.contratos import Contratos
from core.cases.usuario import UsuarioCase
from flask_jwt_extended import create_access_token
from . import np_auth
from .forms import form_login, form_register, form_confirmar_registro


class AuthResource(Resource):
    @np_auth.expect(form_login)
    @validate()
    def post(self, body: Contratos.LoginContrato):
        """Fazer login"""
        try:
            case = UsuarioCase.login(body)
        except UsuarioCase.Exceptions.ConfirmacaoInvalida:
            abort(401, "Login ou senha incorretos")
        return {
            "access_token": create_access_token(
                identity=case.repository.usuario.id,
            )
        }


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
            "usuario_id": str(case.repository.usuario.id),
            "warning": "O ID do usuario, é apenas para teste",
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
