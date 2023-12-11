class NotFoundCinemaException(Exception):
    def __init__(self, message: str = "Cinema não encontrado") -> None:
        super().__init__(message)
        self.message = message
