from .. import db
from ..adapters.type import UUID, generate_uuid
from sqlalchemy import UniqueConstraint


class Assento(db.Model):
    __tablename__ = "Assento"
    __table_args__ = (
        UniqueConstraint(
            "fileira",
            "numero",
            "sala_id",
            name="uq_fileira_numero_sala_id",
        ),
    )

    id = db.Column(UUID, primary_key=True, default=generate_uuid)

    fileira = db.Column(db.String(50), nullable=False)
    numero = db.Column(db.Integer, nullable=False)

    is_ativo = db.Column(db.Boolean, nullable=False, default=True)

    sala_id = db.Column(UUID, db.ForeignKey("Sala.id"), nullable=False)
    sala = db.relationship("Sala", backref="assentos")
