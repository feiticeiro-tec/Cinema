from .. import db
from database.adapters.type import UUID
from sqlalchemy.orm import relationship


class Sessao(db.Model):
    __tablename__ = "Sessao"
    id = db.Column(UUID, primary_key=True)
    dt_inicio = db.Column(db.DateTime, nullable=False)
    dt_fim = db.Column(db.DateTime, nullable=False)

    sala_id = db.Column(UUID, db.ForeignKey("Sala.id"), nullable=False)
    sala = relationship("Sala", backref="sessoes")

    filme_id = db.Column(UUID, db.ForeignKey("Filme.id"), nullable=False)
    filme = relationship("Filme", backref="sessoes")

    dt_criado = db.Column(db.DateTime, nullable=False, default=db.func.now())
