from ...models import Cinema
from .exceptions import NotFoundCinemaException

class CinemaRepository():
    NotFoundCinemaException = NotFoundCinemaException

    def __init__(self, cinema:Cinema= None):
        if not cinema:
            cinema = Cinema()
        self.cinema = cinema
    
    @classmethod
    def use_by_id(cls, id):
        cinema = Cinema.query.filter_by(id=id).first()
        if not cinema:
            raise cls.NotFoundCinemaException()
        return cls(cinema)
    
