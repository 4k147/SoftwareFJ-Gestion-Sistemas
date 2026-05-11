# src/models/servicios/reserva_sala.py
from src.models.servicio import Servicio
from src.exceptions import ServicioError
from src.logger import logger


class ReservaSala(Servicio):
    """Servicio de Reserva de Sala"""

    def __init__(self, nombre: str = "Reserva de Sala", precio_base: float = 150000):
        super().__init__(nombre, precio_base, "Reserva de salas equipadas para reuniones y eventos")

    def calcular_costo(self, duracion_horas: float = 1.0) -> float:
        if duracion_horas <= 0:
            raise ServicioError("La duración debe ser mayor a 0 horas.")
        
        costo = self.precio_base * duracion_horas
        # Descuento por duración larga
        if duracion_horas >= 8:
            costo *= 0.9
        return round(costo, 2)

    def obtener_detalles(self) -> str:
        return (f"🏠 {self.nombre}\n"
                f"   Precio por hora: ${self.precio_base:,}\n"
                f"   Incluye: Proyector, aire acondicionado y wifi")