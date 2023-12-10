from pydantic import BaseModel, validator
from werkzeug.security import generate_password_hash, check_password_hash


class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str

    @validator("senha")
    @classmethod
    def pre_senha(cls, value):
        return generate_password_hash(value)


class LoginContrato(BaseModel):
    email: str
    senha: str

    def check_login(self, hash_password):
        return check_password_hash(hash_password, self.senha)


class ConfirmUsuario(BaseModel):
    token: str
    senha: str


class Contratos:
    CreateContrato = UsuarioCreate
    LoginContrato = LoginContrato
    ConfirmUsuario = ConfirmUsuario
