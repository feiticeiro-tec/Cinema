from ...models import Assento
from .exceptions import NotFoundAssentoException as NotFound


class AssentoRepository:
    NotFoundAssentoException = NotFound

    def __init__(self, assento: Assento = None):
        if not assento:
            assento = Assento()
        self.assento = assento

    @classmethod
    def get_by_id(cls, id):
        assento = Assento.query.filter(Assento.id == id).first()
        if not assento:
            raise cls.NotFoundAssentoException()
        return assento

    @classmethod
    def use_by_id(cls, id):
        return cls(cls.get_by_id(id))
