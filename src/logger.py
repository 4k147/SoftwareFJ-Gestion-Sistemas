# src/logger.py
"""
Sistema de logging robusto para registrar eventos y errores
"""

import logging
import os
from datetime import datetime

# Configuración del logger
def configurar_logger():
    """Configura y retorna el logger del sistema"""
    
    os.makedirs("logs", exist_ok=True)
    
    logger = logging.getLogger("SoftwareFJ")
    logger.setLevel(logging.DEBUG)
    
    # Evitar duplicados de handlers
    if not logger.handlers:
        # Formato detallado
        formatter = logging.Formatter(
            '%(asctime)s | %(levelname)-8s | %(module)s:%(lineno)d | %(message)s'
        )
        
        # Handler para archivo
        file_handler = logging.FileHandler("logs/app.log", encoding='utf-8')
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)
        
        # Handler para consola
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel(logging.INFO)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger


# Instancia global del logger
logger = configurar_logger()