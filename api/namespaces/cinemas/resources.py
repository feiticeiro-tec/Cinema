from flask_restx import Resource, abort
from flask import url_for
from .forms import form_create_cinema
from . import np_cinemas
from flask_jwt_extended import jwt_required, get_jwt_identity
from core.controllers.cinema import (
    CreateCinemaWithColaboradorController,
    CinemaCase,
)
from database.repositorys import CinemaRepository
from flask_pydantic import validate
from pydantic import BaseModel, validator
from flask_restx.reqparse import RequestParser


class QueryOffSetLimit(BaseModel):
    offset: int = 0
    limit: int = 10

    @validator("limit")
    def y(cls, limit):
        if limit > 100:
            raise ValueError("100 é o limite máximo de cinemas por requisição")
        return limit


class CinemasResource(Resource):
    query_model = (
        RequestParser()
        .add_argument("offset", type=int, default=0)
        .add_argument(
            "limit",
            type=int,
            default=10,
            help="O limite máximo de cinemas por requisição é 100",
        )
    )

    @np_cinemas.expect(form_create_cinema)
    @jwt_required()
    @validate()
    @np_cinemas.doc(security="jwt")
    def post(self, body: CinemaCase.Contratos.CreateContrato):
        usuario_id = get_jwt_identity()
        controller = CreateCinemaWithColaboradorController()
        contrato = controller.ExecuteContrato(
            cinema=body,
            usuario_id=usuario_id,
        )
        try:
            case_cinema = controller.execute(contrato)
        except Exception:
            abort(500, message="Um erro inesperado ocorreu")
        uri = url_for(
            "cinemas-target",
            id=case_cinema.repository.cinema.id,
        )
        return (
            {
                "data": {
                    "id": str(case_cinema.repository.cinema.id),
                },
                "_self": uri,
            },
            201,
        )

    @np_cinemas.expect(query_model)
    @validate()
    def get(self, query: QueryOffSetLimit):
        cinemas = CinemaRepository.get_all(
            offset=query.offset,
            limit=query.limit,
        )
        return {
            "data": [
                {
                    "id": str(cinema.id),
                    "nome": cinema.nome,
                    "endereco": {
                        "cep": cinema.cep,
                        "uf": cinema.uf,
                        "cidade": cinema.cidade,
                        "bairro": cinema.bairro,
                        "rua": cinema.rua,
                        "numero": cinema.numero,
                        "complemento": cinema.complemento,
                        "referencia": cinema.referencia,
                    },
                }
                for cinema in cinemas
            ]
        }


class CinemasTargetResource(Resource):
    def get(self, id):
        id = str(id)
        try:
            cinema = CinemaRepository.get_by_id(id)
        except CinemaRepository.NotFoundCinemaException:
            abort(404, message="Cinema não encontrado")
        return {
            "data": {
                "id": str(cinema.id),
                "nome": cinema.nome,
                "endereco": {
                    "cep": cinema.cep,
                    "uf": cinema.uf,
                    "cidade": cinema.cidade,
                    "bairro": cinema.bairro,
                    "rua": cinema.rua,
                    "numero": cinema.numero,
                    "complemento": cinema.complemento,
                    "referencia": cinema.referencia,
                },
            }
        }
