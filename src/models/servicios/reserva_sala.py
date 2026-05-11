from src.models.servicio import Servicio
from src.exceptions import ServicioError
from src.logger import logger


class ReservaSala(Servicio):
    """Servicio de Reserva de Sala"""

    def __init__(self):
        super().__init__("Reserva de Sala", 150000, "Reserva de salas equipadas")

    def calcular_costo(self, duracion_horas: float = 1.0, **kwargs) -> float:
        """Método sobrecargado"""
        if duracion_horas <= 0:
            raise ServicioError("La duración debe ser mayor a 0 horas.")

        costo = self.precio_base * duracion_horas

        # Sobrecarga con parámetros opcionales
        if kwargs.get("aplicar_descuento", True) and duracion_horas >= 8:
            costo *= 0.9
        if impuesto := kwargs.get("impuesto", 0):
            costo *= (1 + impuesto)

        logger.info(f"Costo calculado ReservaSala: ${costo:,} ({duracion_horas}h)")
        return round(costo, 2)

    def obtener_detalles(self) -> str:
        return f"🏠 {self.nombre} - Incluye proyector, AC y WiFi"