# src/exceptions.py
"""
Excepciones personalizadas para el Sistema de Gestión Software FJ
"""

class ErrorSistema(Exception):
    """Excepción base para todos los errores del sistema"""
    pass


class ValidacionError(ErrorSistema):
    """Error cuando los datos ingresados no cumplen las validaciones"""
    pass


class ClienteError(ValidacionError):
    """Errores relacionados con clientes"""
    pass


class ServicioError(ErrorSistema):
    """Errores relacionados con servicios"""
    pass


class ReservaError(ErrorSistema):
    """Errores relacionados con reservas"""
    pass


class ServicioNoDisponibleError(ServicioError):
    """Cuando se intenta reservar un servicio no disponible"""
    pass


class ReservaInvalidaError(ReservaError):
    """Cuando una reserva no puede ser procesada"""
    pass