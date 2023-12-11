from pydantic import BaseModel
from ..cases import CinemaCase, ColaboradorCase


class ExecuteContratoExtensao:
    Cinema = CinemaCase.Contratos.CreateContrato


class ExecuteContrato(BaseModel, ExecuteContratoExtensao):
    cinema: CinemaCase.Contratos.CreateContrato
    usuario_id: str


class CreateCinemaWithColaboradorController:
    ExecuteContrato = ExecuteContrato

    def __init__(
        self,
        case_cinema=None,
        case_colaborador=None,
    ):
        self.case_cinema = case_cinema or CinemaCase()
        self.Endereco = self.case_cinema.repository.Endereco
        self.case_colaborador = case_colaborador or ColaboradorCase()

    def execute(self, contrato: ExecuteContrato):
        case_cinema = self.case_cinema.create(contrato.cinema)
        case_cinema.flush()
        cinema_id = case_cinema.repository.cinema.id
        case_colaborador = self.case_colaborador.create(
            self.case_colaborador.Contratos.CreateContrato(
                usuario_id=contrato.usuario_id,
                cinema_id=cinema_id,
                is_admin=True,
            )
        )
        case_colaborador.commit()
        return case_cinema, case_colaborador
