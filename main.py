# main.py
"""
Sistema Integral de Gestión Software FJ - Fase 4
Punto de entrada principal
"""

from src.logger import logger
from src.models.sistema import SistemaGestion

def main():
    logger.info("🚀 Iniciando Sistema Software FJ - Versión Final")
    
    print("=" * 70)
    print("   BIENVENIDO AL SISTEMA SOFTWARE FJ")
    print("=" * 70)
    
    sistema = SistemaGestion()
    
    try:
        sistema.menu()
    except KeyboardInterrupt:
        print("\n\n👋 Programa terminado por el usuario.")
    except Exception as e:
        logger.critical(f"Error crítico en el sistema: {e}", exc_info=True)
        print("❌ Ocurrió un error grave. Revise el archivo de logs.")

if __name__ == "__main__":
    main()