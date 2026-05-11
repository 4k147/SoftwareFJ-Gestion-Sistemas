# src/models/sistema.py
"""
Clase SistemaGestion - Orquestador principal del sistema
"""

from src.logger import logger
from src.exceptions import ErrorSistema, ValidacionError, ReservaError
from src.models.clientes import Cliente
from src.models.servicios.reserva_sala import ReservaSala
from src.models.servicios.alquiler_equipo import AlquilerEquipo
from src.models.servicios.asesoria import Asesoria
from src.models.reserva import Reserva


class SistemaGestion:
    """Sistema principal de gestión Software FJ"""

    def __init__(self):
        self.clientes = []
        self.reservas = []
        self.servicios = [
            ReservaSala(),
            AlquilerEquipo(),
            Asesoria()
        ]
        logger.info("Sistema de Gestión inicializado")

    def registrar_cliente(self):
        print("\n--- Registro de Nuevo Cliente ---")
        try:
            cedula = input("Cédula: ").strip()
            nombre = input("Nombre: ").strip()
            apellido = input("Apellido: ").strip()
            email = input("Email: ").strip()
            telefono = input("Teléfono: ").strip()
            direccion = input("Dirección (opcional): ").strip()

            cliente = Cliente(cedula, nombre, apellido, email, telefono, direccion)
            self.clientes.append(cliente)
            print(f"✅ Cliente {cliente.get_nombre_completo()} registrado exitosamente.")
            return cliente

        except ValidacionError as e:
            print(f"❌ Error de validación: {e}")
        except Exception as e:
            logger.error(f"Error registrando cliente: {e}")
            print("❌ Error inesperado al registrar cliente.")

    def crear_reserva(self):
        print("\n--- Crear Nueva Reserva ---")
        try:
            if not self.clientes:
                print("⚠️  No hay clientes registrados. Registre uno primero.")
                return

            # Mostrar clientes
            print("Clientes disponibles:")
            for i, c in enumerate(self.clientes, 1):
                print(f"{i}. {c.get_nombre_completo()} - {c.cedula}")

            idx = int(input("\nSeleccione cliente (número): ")) - 1
            if idx < 0 or idx >= len(self.clientes):
                raise ValidacionError("Selección de cliente fuera de rango.")

            cliente = self.clientes[idx]

            # Mostrar servicios
            print("\nServicios disponibles:")
            for i, s in enumerate(self.servicios, 1):
                print(f"{i}. {s.nombre} - ${s.precio_base:,}")

            idx_s = int(input("Seleccione servicio (número): ")) - 1
            if idx_s < 0 or idx_s >= len(self.servicios):
                raise ValidacionError("Selección de servicio fuera de rango.")

            servicio = self.servicios[idx_s]

            duracion = float(input("Duración (horas o días): "))
            
            reserva = Reserva(cliente, servicio, duracion)
            reserva.confirmar()

            self.reservas.append(reserva)
            print("🎉 Reserva creada y confirmada exitosamente.")

        except (ValueError, IndexError):
            logger.error("Entrada inválida en crear_reserva")
            print("❌ Error: Entrada numérica inválida.")
        except ValidacionError as e:
            print(f"❌ Validación: {e}")
        except ReservaError as e:
            print(f"❌ Error en reserva: {e}")
        except Exception as e:
            logger.critical(f"Error grave creando reserva: {e}", exc_info=True)
            print("❌ Error inesperado en el sistema.")

            
    def mostrar_reservas(self):
        print("\n--- Lista de Reservas ---")
        if not self.reservas:
            print("No hay reservas registradas aún.")
            return
        for i, r in enumerate(self.reservas, 1):
            print(f"{i}. {r}")

    def mostrar_clientes(self):
        print("\n--- Lista de Clientes ---")
        if not self.clientes:
            print("No hay clientes registrados.")
            return
        for c in self.clientes:
            print(c)

    def menu(self):
        while True:
            print("\n" + "="*60)
            print("   SISTEMA DE GESTIÓN SOFTWARE FJ")
            print("="*60)
            print("1. Registrar nuevo cliente")
            print("2. Crear nueva reserva")
            print("3. Ver clientes")
            print("4. Ver reservas")
            print("5. Salir")
            print("="*60)

            opcion = input("\nSeleccione una opción: ").strip()

            if opcion == "1":
                self.registrar_cliente()
            elif opcion == "2":
                self.crear_reserva()
            elif opcion == "3":
                self.mostrar_clientes()
            elif opcion == "4":
                self.mostrar_reservas()
            elif opcion == "5":
                print("👋 Gracias por usar Software FJ. ¡Hasta pronto!")
                logger.info("Sistema finalizado por el usuario.")
                break
            else:
                print("❌ Opción inválida. Intente de nuevo.")