from .. import db
from ..adapters.type import UUID, generate_uuid
from ..adapters.functions import datetime_local
from sqlalchemy.orm import relationship


class Ticket(db.Model):
    __tablename__ = "Ticket"
    id = db.Column(UUID, primary_key=True, default=generate_uuid)
    sessao_id = db.Column(UUID, db.ForeignKey("Sessao.id"), nullable=False)
    sessao = relationship("Sessao", backref="tickets")
    usuario_id = db.Column(UUID, db.ForeignKey("Usuario.id"), nullable=False)
    usuario = relationship("Usuario", backref="tickets")
    assento_id = db.Column(UUID, db.ForeignKey("Assento.id"), nullable=False)
    assento = relationship("Assento", backref="tickets")
    is_cancelado = db.Column(db.Boolean, nullable=False, default=False)
    is_usado = db.Column(db.Boolean, nullable=False, default=False)
    dt_criado = db.Column(db.DateTime, nullable=False, default=datetime_local)
