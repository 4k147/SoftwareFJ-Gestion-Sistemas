# src/models/cliente.py
"""
Clase Cliente con encapsulación y validaciones robustas
"""

from datetime import date
import re
from src.exceptions import ClienteError, ValidacionError
from src.logger import logger


class Cliente:
    """
    Representa un cliente del sistema Software FJ.
    Implementa encapsulación con atributos privados.
    """

    def __init__(self, cedula: str, nombre: str, apellido: str, 
                 email: str, telefono: str, direccion: str = ""):
        
        self._cedula = self._validar_cedula(cedula)
        self._nombre = self._validar_nombre(nombre)
        self._apellido = self._validar_nombre(apellido)
        self._email = self._validar_email(email)
        self._telefono = self._validar_telefono(telefono)
        self._direccion = direccion.strip()
        
        logger.info(f"Cliente creado exitosamente: {self._nombre} {self._apellido} (Cédula: {self._cedula})")

    #  VALIDACIONES 

    def _validar_cedula(self, cedula: str) -> str:
        cedula = cedula.strip()
        if not cedula.isdigit():
            logger.error(f"Cédula inválida (debe contener solo números): {cedula}")
            raise ValidacionError("La cédula debe contener solo números.")
        if len(cedula) < 5 or len(cedula) > 12:
            logger.error(f"Cédula con longitud inválida: {cedula}")
            raise ValidacionError("La cédula debe tener entre 5 y 12 dígitos.")
        return cedula

    def _validar_nombre(self, nombre: str) -> str:
        nombre = nombre.strip()
        if not nombre or len(nombre) < 2:
            logger.error(f"Nombre inválido: {nombre}")
            raise ValidacionError("El nombre debe tener al menos 2 caracteres.")
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", nombre):
            logger.error(f"Nombre con caracteres inválidos: {nombre}")
            raise ValidacionError("El nombre solo puede contener letras y espacios.")
        return nombre.title()

    def _validar_email(self, email: str) -> str:
        email = email.strip().lower()
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, email):
            logger.error(f"Email inválido: {email}")
            raise ValidacionError("El email tiene un formato inválido.")
        return email

    def _validar_telefono(self, telefono: str) -> str:
        telefono = re.sub(r'[\s\-\(\)]', '', telefono)  # Limpia formato
        if not telefono.isdigit():
            logger.error(f"Teléfono inválido: {telefono}")
            raise ValidacionError("El teléfono debe contener solo números.")
        if len(telefono) < 7 or len(telefono) > 15:
            logger.error(f"Teléfono con longitud inválida: {telefono}")
            raise ValidacionError("El teléfono debe tener entre 7 y 15 dígitos.")
        return telefono

    #  GETTERS (Encapsulación) 

    @property
    def cedula(self):
        return self._cedula

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def email(self):
        return self._email

    @property
    def telefono(self):
        return self._telefono

    @property
    def direccion(self):
        return self._direccion

    #  MÉTODOS 

    def get_nombre_completo(self) -> str:
        return f"{self._nombre} {self._apellido}"

    def __str__(self):
        return f"Cliente: {self.get_nombre_completo()} | Cédula: {self._cedula} | Email: {self._email}"

    def __repr__(self):
        return f"Cliente(cedula={self._cedula}, nombre={self.get_nombre_completo()})"