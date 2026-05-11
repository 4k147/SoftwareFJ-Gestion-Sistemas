from src.models.servicio import Servicio
from src.exceptions import ServicioError


class AlquilerEquipo(Servicio):
    """Servicio de Alquiler de Equipos"""

    def __init__(self):
        super().__init__("Alquiler de Equipos", 80000, "Alquiler de laptops y equipo audiovisual")

    def calcular_costo(self, dias: int = 1, **kwargs) -> float:
        if dias <= 0:
            raise ServicioError("La cantidad de días debe ser mayor a 0.")

        costo = self.precio_base * dias

        if kwargs.get("aplicar_descuento", True) and dias >= 7:
            costo *= 0.85
        if impuesto := kwargs.get("impuesto", 0):
            costo *= (1 + impuesto)

        return round(costo, 2)

    def obtener_detalles(self) -> str:
        return f"💻 {self.nombre} - Laptops, proyectores y más"