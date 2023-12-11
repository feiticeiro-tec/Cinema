from database.repositorys.colaborador.exceptions import (
    DuplicadoColaboradorException,
)


class ContratoInvalido(Exception):
    ...


class Exceptions:
    Duplicado = DuplicadoColaboradorException
    ContratoInvalido = ContratoInvalido
