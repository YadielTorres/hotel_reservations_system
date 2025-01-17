from flask import Flask
from config import Config
from models import db
from flask_login import LoginManager
from routes.auth_routes import auth_bp
from routes.cliente_routes import cliente_bp
from routes.habitacion_routes import habitacion_bp
from routes.reserva_routes import reserva_bp

app= Flask(__name__)
app.config.from_object(Config)

#Configurar la base de datos
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'
# Registrar Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(cliente_bp, url_prefix='/clientes')
app.register_blueprint(habitacion_bp, url_prefix='/habitaciones')
app.register_blueprint(reserva_bp, url_prefix='/reservas')


@app.route('/')
def hello():
	return 'Capa de Logica de Negocio - Flask funcionando'
	
	
def get_connection():
    connection = pymysql.connect(
        host= '192.168.17.135',
        user='host_user',
        password='secure_password',
        db='hotel_reservations',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection    
    
    
@login_manager.user_loader
def load_user(user_id):
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = %s",(user_id,))
    row = cursor.fetchone()
    if row:
        return Usuario(id=row[0], email=row[1], password=row[2], nombre=row[3], rol=row[4])
    else:
        return None
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
'''
@app.route('/')
def hello():
	return 'Capa de Logica de Negocio - Flask funcionando'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)

def get_connection():
    connection = pymysql.connect(
        host= '192.168.17.135',
        user='host_user'
        password='secure_password',
        db='hotel_reservations',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

'''

