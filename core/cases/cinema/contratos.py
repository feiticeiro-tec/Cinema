from pydantic import BaseModel
from database.repositorys import CinemaRepository


class CreateContratoExtensao:
    Endereco = CinemaRepository.Endereco


class CreateContrato(BaseModel, CreateContratoExtensao):
    nome: str
    descricao: str
    endereco: CinemaRepository.Endereco


class Contratos:
    CreateContrato = CreateContrato
