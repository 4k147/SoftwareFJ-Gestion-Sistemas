# src/logger.py
"""
Sistema de logging profesional - Solo errores en consola, todo en archivo
"""

import logging
import os
from datetime import datetime

def configurar_logger():
    """Configura el logger: INFO+ en archivo, solo WARNING+ en consola"""
    
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger("SoftwareFJ")
    logger.setLevel(logging.DEBUG)
    
    
    if logger.handlers:
        return logger

    
    file_formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(module)s:%(lineno)d | %(message)s'
    )
    

    console_formatter = logging.Formatter(
        '%(levelname)s | %(message)s'
    )

    # Handler para archivo (guarda TODO)
    file_handler = logging.FileHandler("logs/app.log", encoding='utf-8')
    file_handler.setFormatter(file_formatter)
    file_handler.setLevel(logging.DEBUG)

    # Handler para consola (solo warnings y errores)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(console_formatter)
    console_handler.setLevel(logging.WARNING)   # ← Cambiado aquí

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger



logger = configurar_logger()