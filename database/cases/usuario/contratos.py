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
