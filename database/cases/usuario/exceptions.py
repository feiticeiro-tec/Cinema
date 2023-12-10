from database.repositorys.usuario.excpetions import UsuarioDuplicado

class ContratoInvalido(Exception):
    pass


class ConfirmacaoInvalida(Exception):
    pass


class UsuarioInativado(Exception):
    pass

class Exceptions():
    ContratoInvalido = ContratoInvalido
    ConfirmacaoInvalida = ConfirmacaoInvalida
    UsuarioInativado = UsuarioInativado
    UsuarioDuplicado = UsuarioDuplicado