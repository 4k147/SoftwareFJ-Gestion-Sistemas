# main.py
"""
SOFTWARE FJ - Sistema Integral de Gestión
Trabajo Fase 4 - Programación Orientada a Objetos
Universidad Nacional Abierta y a Distancia (UNAD)
"""

from src.logger import logger
from src.models.sistema import SistemaGestion

def mostrar_banner():
    print("=" * 70)
    print(" " * 15 + "SOFTWARE FJ - GESTIÓN DE SERVICIOS")
    print("=" * 70)
    print("Sistema desarrollado con:")
    print("• Programación Orientada a Objetos")
    print("• Manejo Avanzado de Excepciones")
    print("• Principios SOLID (parcialmente)")
    print("• Logging profesional")
    print("=" * 70)

def main():
    logger.info("=== INICIO DE EJECUCIÓN DEL SISTEMA ===")
    
    mostrar_banner()
    
    sistema = SistemaGestion()
    
    try:
        sistema.menu()
    except KeyboardInterrupt:
        print("\n\n👋 Programa terminado por el usuario.")
        logger.info("Sistema finalizado por KeyboardInterrupt")
    except Exception as e:
        logger.critical(f"Error crítico no controlado: {e}", exc_info=True)
        print("\n❌ Error grave. Revise el archivo logs/app.log")
    finally:
        logger.info("=== FIN DE EJECUCIÓN DEL SISTEMA ===")
        print("\nGracias por usar Software FJ")

if __name__ == "__main__":
    main()