from src.models.servicio import Servicio
from src.exceptions import ServicioError


class Asesoria(Servicio):
    """Servicio de Asesoría Especializada"""

    def __init__(self):
        super().__init__("Asesoría Especializada", 250000, "Consultorías técnicas")

    def calcular_costo(self, horas: float = 1.0, **kwargs) -> float:
        if horas <= 0:
            raise ServicioError("La duración debe ser mayor a 0 horas.")

        costo = self.precio_base * horas

        if kwargs.get("recargo_experto", False) and horas >= 5:
            costo *= 1.12
        if impuesto := kwargs.get("impuesto", 0):
            costo *= (1 + impuesto)

        return round(costo, 2)

    def obtener_detalles(self) -> str:
        return f"👨‍💼 {self.nombre} - Desarrollo, Gestión y Ciberseguridad"