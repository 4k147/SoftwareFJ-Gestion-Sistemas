# src/models/reserva.py
"""
Clase Reserva - Integra Cliente y Servicio con manejo de estados y excepciones
"""

from datetime import datetime
from src.exceptions import ReservaError, ReservaInvalidaError
from src.logger import logger
from src.models.clientes import Cliente
from src.models.servicio import Servicio


class Reserva:
    """Representa una reserva en el sistema Software FJ"""

    ESTADOS = ["pendiente", "confirmada", "cancelada", "completada"]

    def __init__(self, cliente: Cliente, servicio: Servicio, duracion: float):
        
        self._cliente = self._validar_cliente(cliente)
        self._servicio = self._validar_servicio(servicio)
        self._duracion = self._validar_duracion(duracion)
        self._estado = "pendiente"
        self._fecha_reserva = datetime.now()
        self._costo_total = None

        logger.info(f"Nueva reserva creada - Cliente: {cliente.get_nombre_completo()} | Servicio: {servicio.nombre}")

    # ==================== VALIDACIONES ====================

    def _validar_cliente(self, cliente):
        if not isinstance(cliente, Cliente):
            logger.error("Intento de crear reserva sin un Cliente válido")
            raise ReservaInvalidaError("Se requiere un objeto Cliente válido.")
        return cliente

    def _validar_servicio(self, servicio):
        if not isinstance(servicio, Servicio):
            logger.error("Intento de crear reserva sin un Servicio válido")
            raise ReservaInvalidaError("Se requiere un objeto Servicio válido.")
        return servicio

    def _validar_duracion(self, duracion: float) -> float:
        if duracion <= 0:
            logger.error(f"Duración inválida: {duracion}")
            raise ReservaInvalidaError("La duración debe ser mayor a 0.")
        return round(duracion, 2)

    # ==================== PROPIEDADES ====================

    @property
    def cliente(self):
        return self._cliente

    @property
    def servicio(self):
        return self._servicio

    @property
    def duracion(self):
        return self._duracion

    @property
    def estado(self):
        return self._estado

    @property
    def costo_total(self):
        return self._costo_total

    @property
    def fecha_reserva(self):
        return self._fecha_reserva

    # ==================== MÉTODOS ====================

    def calcular_costo(self) -> float:
        """Calcula el costo usando polimorfismo del servicio"""
        try:
            self._costo_total = self._servicio.calcular_costo(self._duracion)
            logger.info(f"Costo calculado: ${self._costo_total:,} para reserva de {self._servicio.nombre}")
            return self._costo_total
        except Exception as e:
            logger.error(f"Error calculando costo: {e}")
            raise ReservaError(f"Error al calcular costo: {e}") from e

    def confirmar(self):
        """Confirma la reserva"""
        if self._estado != "pendiente":
            raise ReservaError(f"No se puede confirmar una reserva en estado: {self._estado}")
        
        self.calcular_costo()
        self._estado = "confirmada"
        logger.info(f"Reserva CONFIRMADA - Cliente: {self._cliente.get_nombre_completo()}")
        print(f"✅ Reserva confirmada por {self._cliente.get_nombre_completo()}")
        return True

    def cancelar(self):
        """Cancela la reserva"""
        if self._estado == "completada":
            raise ReservaError("No se puede cancelar una reserva ya completada.")
        
        self._estado = "cancelada"
        logger.warning(f"Reserva CANCELADA - Cliente: {self._cliente.get_nombre_completo()}")
        print("❌ Reserva cancelada exitosamente.")
        return True

    def completar(self):
        """Marca la reserva como completada"""
        if self._estado != "confirmada":
            raise ReservaError("Solo se pueden completar reservas confirmadas.")
        
        self._estado = "completada"
        logger.info(f"Reserva COMPLETADA - Cliente: {self._cliente.get_nombre_completo()}")
        print("🏁 Reserva marcada como completada.")
        return True

    def __str__(self):
        return (f"Reserva | Estado: {self._estado.upper()} | "
                f"Cliente: {self._cliente.get_nombre_completo()} | "
                f"Servicio: {self._servicio.nombre} | "
                f"Duración: {self._duracion} | "
                f"Costo: ${self._costo_total if self._costo_total else 'Pendiente'}")

    def __repr__(self):
        return f"Reserva(cliente={self._cliente.cedula}, servicio={self._servicio.nombre}, estado={self._estado})"