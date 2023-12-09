from .. import db
from database.adapters.type import UUID
from database.adapters.functions import datetime_local
from sqlalchemy.orm import relationship

class Ticket(db.Model):
    id = db.Column(UUID, primary_key=True)
    sessao_id = db.Column(UUID, db.ForeignKey("Sessao.id"), nullable=False)
    sessao = relationship("Sessao", backref="tickets")
    usuario_id = db.Column(UUID, db.ForeignKey("Usuario.id"), nullable=False)
    usuario = relationship("Usuario", backref="tickets")
    assento_id = db.Column(UUID, db.ForeignKey("Assento.id"), nullable=False)
    assento = relationship("Assento", backref="tickets")
    is_cancelado = db.Column(db.Boolean, nullable=False, default=False)
    is_usado = db.Column(db.Boolean, nullable=False, default=False)
    dt_criado = db.Column(db.DateTime, nullable=False, default=datetime_local)

