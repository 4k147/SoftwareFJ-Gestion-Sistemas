# src/models/servicio.py
"""
Clase Abstracta Servicio - Base para todos los servicios
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
            logger.error(f"Precio inválido: {precio}")
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

    # ==================== MÉTODOS ABSTRACTOS (Polimorfismo) ====================

    @abstractmethod
    def calcular_costo(self, duracion: float = 1.0) -> float:
        """Calcula el costo total según el tipo de servicio"""
        pass

    @abstractmethod
    def obtener_detalles(self) -> str:
        """Retorna detalles específicos del servicio"""
        pass

    # ==================== MÉTODO COMÚN ====================

    def __str__(self):
        return f"Servicio: {self._nombre} | Precio base: ${self._precio_base:,}"

    def __repr__(self):
        return f"{self.__class__.__name__}(nombre={self._nombre})"