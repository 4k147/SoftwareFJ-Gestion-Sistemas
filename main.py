# main.py
from src.logger import logger
from src.exceptions import ErrorSistema, ReservaError, ValidacionError
from src.models.clientes import Cliente
from src.models.servicios.reserva_sala import ReservaSala
from src.models.servicios.alquiler_equipo import AlquilerEquipo
from src.models.servicios.asesoria import Asesoria
from src.models.reserva import Reserva

def probar_reserva():
    print("=" * 80)
    print("   PRUEBA DE CLASE RESERVA - PASO 4")
    print("=" * 80)
    
    try:
        # Crear cliente y servicio
        cliente = Cliente("987654321", "María", "González", "maria.g@email.com", "3109876543")
        sala = ReservaSala()

        # Crear reserva
        reserva = Reserva(cliente=cliente, servicio=sala, duracion=6)

        print("✅ Reserva creada:")
        print(reserva)
        print()

        # Operaciones
        reserva.calcular_costo()
        reserva.confirmar()
        print(reserva)

        # Prueba de error (intentar cancelar después de confirmar)
        # reserva.cancelar()   # Puedes descomentar para probar

    except ValidacionError as e:
        print(f"✅ Validación correcta: {e}")
    except ReservaError as e:
        logger.warning(f"Error controlado en reserva: {e}")
        print(f"⚠️  Error controlado: {e}")
    except Exception as e:
        logger.error(f"Error inesperado: {e}")

def main():
    logger.info("🚀 Iniciando Paso 4 - Clase Reserva")
    try:
        probar_reserva()
        print("\n🎉 ¡Paso 4 completado exitosamente!")
    except Exception as e:
        logger.critical(f"Error grave: {e}", exc_info=True)

if __name__ == "__main__":
    main()