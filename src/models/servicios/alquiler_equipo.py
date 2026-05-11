# src/models/servicios/alquiler_equipo.py
from src.models.servicio import Servicio
from src.exceptions import ServicioError
from src.logger import logger


class AlquilerEquipo(Servicio):
    """Servicio de Alquiler de Equipos"""

    def __init__(self, nombre: str = "Alquiler de Equipos", precio_base: float = 80000):
        super().__init__(nombre, precio_base, "Alquiler de laptops, proyectores y equipo audiovisual")

    def calcular_costo(self, dias: int = 1) -> float:
        if dias <= 0:
            raise ServicioError("La cantidad de días debe ser mayor a 0.")
        
        costo = self.precio_base * dias
        # Descuento por alquiler prolongado
        if dias >= 7:
            costo *= 0.85
        return round(costo, 2)

    def obtener_detalles(self) -> str:
        return (f"💻 {self.nombre}\n"
                f"   Precio por día: ${self.precio_base:,}\n"
                f"   Equipos disponibles: Laptops, Proyectores, Pantallas")