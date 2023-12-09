from .. import db
from database.adapters.type import UUID, generate_uuid
from sqlalchemy import UniqueConstraint


class Assento(db.Model):
    __tablename__ = "Assento"
    __table_args__ = (
        UniqueConstraint(
            "assento",
            "sala_id",
            name="uq_assento_sala",
        ),
    )

    id = db.Column(UUID, primary_key=True, default=generate_uuid)
    assento = db.Column(db.String(50), nullable=False)
    is_ativo = db.Column(db.Boolean, nullable=False, default=True)

    sala_id = db.Column(UUID, db.ForeignKey("Sala.id"), nullable=False)
    sala = db.relationship("Sala", backref="assentos")
