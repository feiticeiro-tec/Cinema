from pydantic import BaseModel, field_validator, field_serializer
from werkzeug.security import generate_password_hash, check_password_hash


class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str

    @field_validator("senha")
    @classmethod
    def pre_senha(cls, value):
        return generate_password_hash(value)


class LoginContrato(BaseModel):
    email: str
    senha: str

    def check_login(self, hash_password):
        return check_password_hash(hash_password, self.senha)


class Contratos:
    CreateContrato = UsuarioCreate
    LoginContrato = LoginContrato
