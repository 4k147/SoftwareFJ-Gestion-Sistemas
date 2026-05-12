# 🚀 Software FJ - Sistema de Gestión de Servicios

**Trabajo Final - Fase 4**  
**Programación Orientada a Objetos**  
**Universidad Nacional Abierta y a Distancia (UNAD)**

---

## 📋 Descripción del Proyecto

Sistema integral desarrollado en **Python** utilizando **Programación Orientada a Objetos (POO)** para la gestión de clientes, servicios y reservas de la empresa **Software FJ**.

El sistema permite registrar clientes, crear reservas de salas, alquiler de equipos y asesorías especializadas, todo esto sin utilizar bases de datos (solo objetos en memoria y archivos de logs).

---

## ✨ Características Principales

- **Abstracción**: Clase abstracta `Servicio`
- **Herencia**: Tres servicios que heredan de la clase abstracta
- **Polimorfismo**: Método `calcular_costo()` con comportamiento diferente
- **Encapsulación**: Atributos privados en la clase `Cliente`
- **Manejo Avanzado de Excepciones**: Excepciones personalizadas + bloques `try/except/else/finally`
- **Logging Profesional**: Registro detallado de eventos y errores
- **Validaciones Robustas**: Control de datos inválidos
- **Métodos Sobrecargados** (simulados con `**kwargs`)
- **Interfaz de Menú** interactiva

---

## 🛠️ Tecnologías Utilizadas

- **Python 3**
- Programación Orientada a Objetos
- Módulos y paquetes
- Manejo de archivos (logs)
- Excepciones personalizadas

---

## 📁 Estructura del Proyecto

```bash
SoftwareFJ-Gestion-Sistemas/
├── main.py                 
├── tests.py                
├── README.md
├── logs/
│   └── app.log             
└── src/
    ├── exceptions.py
    ├── logger.py
    └── models/
        ├── cliente.py
        ├── reserva.py
        ├── servicio.py
        ├── sistema.py
        └── servicios/