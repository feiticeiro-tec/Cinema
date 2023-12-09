from .. import db


class EnderecoModel(db.Model):
    __abstract__ = True

    cep = db.Column(db.String(8), nullable=False)
    uf = db.Column(db.String(2), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    bairro = db.Column(db.String(100), nullable=False)
    rua = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.Integer, nullable=False)
    complemento = db.Column(db.String(100), nullable=True)
    referencia = db.Column(db.String(100), nullable=True)
