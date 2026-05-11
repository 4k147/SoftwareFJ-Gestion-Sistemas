# src/models/servicio.py
"""
Clase Abstracta Servicio con polimorfismo y sobrecarga simulada
"""

from abc import ABC, abstractmethod
from datetime import datetime
from src.exceptions import ServicioError
from src.logger import logger


class Servicio(ABC):
    """Clase abstracta que representa un servicio de Software FJ"""

    def __init__(self, nombre: str, precio_base: float, descripcion: str = ""):
        self._nombre = nombre.strip()
        self._precio_base = self._validar_precio(precio_base)
        self._descripcion = descripcion.strip() or "Sin descripción disponible"
        self._fecha_creacion = datetime.now()

        logger.info(f"Servicio creado: {self._nombre} (Precio base: ${self._precio_base})")

    def _validar_precio(self, precio: float) -> float:
        if precio <= 0:
            raise ServicioError("El precio base debe ser mayor a cero.")
        return round(precio, 2)

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio_base(self):
        return self._precio_base

    @property
    def descripcion(self):
        return self._descripcion

    # ==================== MÉTODO SOBRECARGADO====================
    @abstractmethod
    def calcular_costo(self, duracion: float = 1.0, **kwargs) -> float:
        """
        Método sobrecargado (simulado):
        - duracion: horas o días
        - kwargs: aplicar_descuento, impuesto, etc.
        """
        pass

    @abstractmethod
    def obtener_detalles(self) -> str:
        pass

    def __str__(self):
        return f"Servicio: {self._nombre} | Precio base: ${self._precio_base:,}"