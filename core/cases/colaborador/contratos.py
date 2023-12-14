from pydantic import BaseModel


class CreateContrato(BaseModel):
    usuario_id: str
    cinema_id: str
    is_admin: bool = False


class Contratos:
    CreateContrato = CreateContrato
