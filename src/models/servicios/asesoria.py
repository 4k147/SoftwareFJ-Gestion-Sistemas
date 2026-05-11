# src/models/servicios/asesoria.py
from src.models.servicio import Servicio
from src.exceptions import ServicioError


class Asesoria(Servicio):
    """Servicio de Asesoría Especializada"""

    def __init__(self, nombre: str = "Asesoría Especializada", precio_base: float = 250000):
        super().__init__(nombre, precio_base, "Asesorías técnicas y consultorías especializadas")

    def calcular_costo(self, horas: float = 1.0) -> float:
        if horas <= 0:
            raise ServicioError("La duración debe ser mayor a 0 horas.")
        
        costo = self.precio_base * horas
        # Recargo por asesor senior
        if horas >= 5:
            costo *= 1.1
        return round(costo, 2)

    def obtener_detalles(self) -> str:
        return (f"👨‍💼 {self.nombre}\n"
                f"   Tarifa por hora: ${self.precio_base:,}\n"
                f"   Áreas: Desarrollo de software, Gestión de proyectos, Ciberseguridad")