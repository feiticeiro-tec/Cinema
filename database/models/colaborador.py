from .. import db
from database.adapters.type import UUID
from database.adapters.functions import datetime_local
from sqlalchemy.orm import relationship

class Colaborador(db.Model):
    __tablename__ = "Colaborador"
    id = db.Column(UUID, primary_key=True)
    usuario_id = db.Column(UUID, db.ForeignKey("Usuario.id"), nullable=False)
    usuario = relationship("Usuario", backref="colaboradores")
    cinema_id = db.Column(UUID, db.ForeignKey("Cinema.id"), nullable=False)
    cinema = relationship("Cinema", backref="colaboradores")
    is_ativo = db.Column(db.Boolean, nullable=False, default=True)
    dt_criado = db.Column(db.Datetime, nullable=False, default=datetime_local)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)