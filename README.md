# Sistema de Reservas de Hotel

Este proyecto académico consiste en un sistema de reservas de hotel. La aplicación facilita a los clientes registrarse, acceder a su cuenta y reservar habitaciones. Por su parte, los administradores tienen la capacidad de gestionar las habitaciones y consultar las reservas realizadas.

## Arquitectura del Proyecto
La aplicación está dividida en tres capas, cada una desplegada en una máquina virtual (VM) separada:

1. **Capa de Presentación** (VM1)
- **Tecnologías**: HTML, CSS, Bootstrap, jQuery, jQuery
DataTables
- **Servidor Web**: NGINX
- **Descripción**: Interfaz de usuario accesible desde elexterior a través de SERVEO.

2. **Capa de Lógica de Negocio** (VM2)
- **Tecnologías**: Python Flask
- **Descripción**: API RESTful que maneja la lógica de la
aplicación y se comunica con la base de datos.
3. **Capa de Datos** (VM3)
- **Tecnologías**: MariaDB
- **Descripción**: Base de datos que almacena la información
de clientes, habitaciones y reservas.
## Requisitos Previos
- **Git**
- **Python 3**
- **Pip**
- **NGINX**
- **MariaDB**
- **Acceso a SERVEO** para exponer la aplicación al exterior.
## Instalación y Configuración

### Capa de Presentación (VM1)
- ● Clonar el repositorio:
- git clone https://github.com/tu_usuario/hotel_reservations_system.git
- Navegar al directorio de la capa de presentación:
- cd hotel_reservations_system/presentation_layer
- ● Configurar NGINX según las instrucciones en
- presentation_layer/README.md.
- ● Ejecutar SERVEO para exponer la aplicación.


### Capa de Lógica de Negocio (VM2)
- ● Clonar el repositorio y navegar al directorio correspondiente.
- Crear un entorno virtual y activar:
- python3 -m venv venv
- source venv/bin/activate
- Instalar las dependencias:
- pip install -r requirements.txt
- ● Configurar las variables de entorno y la conexión a la base de datos.
- Ejecutar la aplicación Flask: python app.py

### Capa de Datos (VM3)
- ●Clonar el repositorio y navegar a data_layer/.
- Importar los scripts SQL para crear la base de datos:
- mysql -u usuario -p < sql_scripts/create_database.sql
- Asegurar que la base de datos está configurada y accesible desde VM2.
-
### Estructura del Proyecto

- data_layer/sql_scripts/
- create_database.sql
- usuarios.sql
  
### Cómo Ejecutar la Aplicación
- Luego de correr el archivo create_database.sql, tendra que correr el archivo usuarios.sql para importar la tabla de usuarios


### Autores
- Yadiel Torres - Capa de Datos
- Yadiel Torres - Lógica de Negocio
- Yadiel Torres - Capa de Presentación
