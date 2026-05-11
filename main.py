# main.py
from src.logger import logger
from src.exceptions import ErrorSistema, ServicioError
from src.models.clientes import Cliente
from src.models.servicio import Servicio
from src.models.servicios.reserva_sala import ReservaSala
from src.models.servicios.alquiler_equipo import AlquilerEquipo
from src.models.servicios.asesoria import Asesoria


def probar_servicios():
    print("=" * 75)
    print("   PRUEBA DE SERVICIOS - PASO 3 (Polimorfismo)")
    print("=" * 75)
    
    try:
        # Crear servicios
        sala = ReservaSala()
        equipo = AlquilerEquipo()
        asesoria = Asesoria()

        print("✅ Servicios creados:")
        print(sala)
        print(equipo)
        print(asesoria)
        print()

        # Demostración de polimorfismo
        print("🔄 Demostración de Polimorfismo (calcular_costo):")
        print(f"Reserva Sala (4 horas)  → ${sala.calcular_costo(4):,}")
        print(f"Alquiler Equipo (5 días) → ${equipo.calcular_costo(5):,}")
        print(f"Asesoría (3 horas)       → ${asesoria.calcular_costo(3):,}")
        
    except ServicioError as e:
        logger.warning(f"Error controlado en servicio: {e}")
        print(f"✅ Validación correcta: {e}")

def main():
    logger.info("🚀 Iniciando Paso 3 - Servicios")
    try:
        probar_servicios()
        print("\n🎉 ¡Paso 3 completado exitosamente!")
        print("   Clase abstracta + Polimorfismo implementados.")
    except Exception as e:
        logger.critical(f"Error en Paso 3: {e}", exc_info=True)

if __name__ == "__main__":
    main()