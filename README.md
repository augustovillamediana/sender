# sender

Este proyecto es una aplicación web desarrollada en Flask que te permite lanzar diferentes tipos de campañas de envío de mensajes y correos electrónicos, dependiendo de la API seleccionada y una base de datos SQLite o MariaDB.

## Características

- Interfaz de usuario intuitiva para gestionar campañas.
- Integración con API para el envío de mensajes y correos electrónicos.
- Almacenamiento de datos en una base de datos SQLite o MariaDB.
- Gestión de usuarios con autenticación y autorización.
- Registro de actividades y seguimiento de campañas.

## Requisitos

- Python 3.x
- Flask
- SQLite (para la base de datos) o MariaDB
- Dependencias adicionales (ver `requirements.txt`)

## Instalación

1. Clona este repositorio en tu máquina local:

2. Accede al directorio del proyecto:

   ```
   cd sender
   ```

3. Crea un entorno virtual e instala las dependencias:

   ```
   python -m venv venv
   source venv/bin/activate  # En Windows, usa 'venv\Scripts\activate'
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno en un archivo `.env` (ver `env.example` para detalles).

5. Inicializa la base de datos:

   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. Ejecuta la aplicación:

   ```
   flask run
   ```

La aplicación estará disponible en [http://localhost:5000](http://localhost:5000).

## Uso

1. Accede a la aplicación en tu navegador.
2. Inicia sesión con el usuario y contraceña seleccionado.
3. Crea una nueva campaña seleccionando el tipo de envío (llamadas, mensajes o correos electrónicos), destinatarios y contenido.
4. Lanza la campaña y sigue su progreso desde el panel de control.

## Licencia

Este proyecto está bajo la Licencia GNU GENERAL PUBLIC LICENSE. Consulta el archivo [LICENSE](LICENSE) para obtener más detalles.

---
