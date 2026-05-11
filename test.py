# tests.py
from src.logger import logger
from src.models.clientes import Cliente
from src.models.servicios.reserva_sala import ReservaSala
from src.models.servicios.alquiler_equipo import AlquilerEquipo
from src.models.servicios.asesoria import Asesoria
from src.models.reserva import Reserva
from src.exceptions import *

def pruebas_robustez():
    print("="*80)
    print("   PRUEBAS DE ROBUSTEZ Y MANEJO DE ERRORES")
    print("="*80)
    
    pruebas = 0
    exitos = 0

    try:
        # 1-2 Pruebas válidas
        cliente = Cliente("111222333", "Carlos", "Ramírez", "carlos@test.com", "3205556677")
        sala = ReservaSala()
        reserva1 = Reserva(cliente, sala, 4)
        reserva1.confirmar()
        exitos += 1
        pruebas += 1

        # 3-6 Pruebas de errores (deben ser capturados)
        try:
            Cliente("abc", "Ana", "Lopez", "malo", "123")
        except Exception:
            exitos += 1
        pruebas += 1

        try:
            Reserva(cliente, sala, -5)
        except Exception:
            exitos += 1
        pruebas += 1

        # Más pruebas...
        print(f"\n✅ {exitos}/{pruebas} pruebas de robustez pasadas.")
        logger.info("Pruebas de robustez completadas exitosamente")

    except Exception as e:
        logger.error(f"Error en pruebas: {e}")

if __name__ == "__main__":
    pruebas_robustez()
