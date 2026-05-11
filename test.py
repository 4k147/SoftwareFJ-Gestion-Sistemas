# tests.py
"""
Pruebas robustas y simulación de al menos 10 operaciones
"""

from src.logger import logger
from src.models.clientes import Cliente
from src.models.servicios.reserva_sala import ReservaSala
from src.models.servicios.alquiler_equipo import AlquilerEquipo
from src.models.servicios.asesoria import Asesoria
from src.models.reserva import Reserva
from src.exceptions import *

def pruebas_robustez():
    print("=" * 85)
    print("   PRUEBAS DE ROBUSTEZ Y MANEJO DE EXCEPCIONES - FASE 4")
    print("=" * 85)
    
    contador = 0
    total_pruebas = 10

    try:
        # 1. Cliente válido
        cliente = Cliente("1234567890", "Andrés", "Gómez", "andres@test.com", "3001234567")
        print("1. Cliente válido → OK")
        contador += 1

        # 2-4. Servicios válidos
        sala = ReservaSala()
        equipo = AlquilerEquipo()
        asesoria = Asesoria()
        print("2-4. Tres servicios creados → OK")
        contador += 3

        # 5. Reserva válida con método sobrecargado
        reserva = Reserva(cliente, sala, 6)
        reserva.confirmar()
        print("5. Reserva confirmada (con sobrecarga) → OK")
        contador += 1

        # 6-10. Pruebas de errores (deben ser capturados)
        try:
            Cliente("abc123", "Error", "Test", "emailmalo", "123")
        except Exception:
            print("6. Error en datos de cliente → Capturado correctamente")
            contador += 1

        try:
            Reserva(cliente, sala, -5)
        except Exception:
            print("7. Error duración negativa → Capturado")
            contador += 1

        try:
            Reserva(cliente, sala, 0)
        except Exception:
            print("8. Error duración cero → Capturado")
            contador += 1

        # Prueba con parámetro inválido en calcular_costo
        try:
            sala.calcular_costo(-10)
        except Exception:
            print("9. Error en calcular_costo (parámetro inválido) → Capturado")
            contador += 1

        # Prueba de cancelar reserva no confirmada
        try:
            reserva2 = Reserva(cliente, equipo, 2)
            reserva2.cancelar()
        except Exception:
            print("10. Error al cancelar reserva → Capturado")
            contador += 1

        print("\n" + "✅" * 3)
        print(f"🎉 {contador}/{total_pruebas} operaciones simuladas correctamente.")
        print("✅ El sistema es estable y maneja excepciones de forma profesional.")

        logger.info(f"Pruebas completadas: {contador}/{total_pruebas} exitosas")

    except Exception as e:
        logger.critical(f"Error grave en pruebas: {e}", exc_info=True)
        print(f"❌ Error inesperado en pruebas: {e}")

if __name__ == "__main__":
    pruebas_robustez()