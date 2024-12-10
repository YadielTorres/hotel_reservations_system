#routes/auth_routes.py
from flask import Blueprint, render_template, redirect, url_for,request,flash
from flask_login import login_user, logout_user, login_required
from models import db
from models.cliente import Cliente

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    #Manejar el formulario de login
    pass
@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

from werkzeug.security import generate_password_hash, check_password_hash

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # Manejar el registro de usuarios
    pass
    
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cursor = db.connection.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE email =%s", (email,))
        row = cursor.fetchone()
        if row and check_password_hash(row[2], password):
            user = Usuario(id=row[0], email=row[1], password=row[2], nombre=row[3], rol=row[4])
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Credenciales inválidas')
    return render_template('login.html')
