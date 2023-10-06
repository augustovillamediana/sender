# Configuración general de la aplicación

SECRET_KEY = 'tu_clave_secreta'  # Cambia esto por una clave segura en producción
DEBUG = True  # Activa o desactiva el modo de depuración según sea necesario
DB_TYPE = 'sqlite'  # Puedes cambiar esto a 'mysql' si deseas utilizar MySQL

# Configuración de la base de datos SQLite
if DB_TYPE == 'sqlite':
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'

# Configuración de la base de datos MySQL (solo si DB_TYPE == 'mysql')
if DB_TYPE == 'mysql':
    DB_USERNAME = 'usuario_mysql'
    DB_PASSWORD = 'contraseña_mysql'
    DB_HOST = 'localhost'
    DB_NAME = 'nombre_base_de_datos'

# Otras configuraciones específicas de tu aplicación (por ejemplo, correo electrónico, rutas, etc.)
