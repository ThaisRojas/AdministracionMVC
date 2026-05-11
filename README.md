# FerryCore Admin - Sistema de Administración MVC

Autor: Thais Rojas Torres  
Materia: Ingeniería Web  

## Descripción del Proyecto
Este repositorio contiene el módulo de Administración basado en la arquitectura MVC para alimentar el "Core" del sistema de Reservas de Tickets de Ferry. Permite la creación y programación de viajes garantizando la integridad de los datos.

## Cumplimiento de Requerimientos

### 1. Validación Backend de Dato Sensible 
El dato sensible definido es la **Fecha de Salida** del viaje. 
Se implementó una validación estricta en el controlador (Backend) de Flask (`app.py`). Incluso si un usuario manipula el DOM o quita las restricciones del input de fecha en el HTML, el servidor bloquea cualquier intento de guardar un viaje con una fecha en el pasado, retornando un mensaje de error y protegiendo la base de datos.

### 2. Dropdown Dinámico (Claves Foráneas) 
Para asegurar la integridad referencial al momento de asignar una ruta, se implementaron selectores dependientes (Dropdowns).
- Al seleccionar la Isla de **Origen**, mediante JavaScript (Fetch API) se envía una solicitud al Backend.
- El servidor retorna en formato JSON únicamente las Islas de **Destino** válidas.
- Se evita la inserción manual de IDs.

## Instalación y Despliegue
Para correr este proyecto en local:
1. Clonar el repositorio: `git clone <tu-url>`
2. Crear un entorno virtual: `python -m venv venv`
3. Instalar dependencias: `pip install flask` (y otras librerías necesarias).
4. Ejecutar: `python app.py`

Link del Proyecto Deployado: