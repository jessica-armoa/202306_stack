from flask import render_template, request, redirect, session, flash

from flask_bcrypt import Bcrypt
from flask_app import app
bcrypt = Bcrypt(app)

from flask_app.models.user import User

@app.route("/")
def inicio():
    return render_template("log.html")

@app.route('/register', methods=['POST'])
def register():
    # validar el formulario
    if not User.validate_user(request.form):
        # redirigimos a la plantilla con el formulario
        return redirect('/')
    # crear el hash
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # poner pw_hash en el diccionario de datos
    data = {
        "first_name" : request.form['first_name'],
        "last_name": request.form['last_name'],
        "email" : request.form['email'],
        "password" : pw_hash
    }
    user_id = User.save(data)
    # almacenar id de usuario en la sesión
    session['user_id'] = user_id
    return redirect("/recipes")

@app.route('/login', methods=['POST'])
def login():
    # ver si el nombre de usuario proporcionado existe en la base de datos
    user_in_db = User.get_by_email(request.form["email"])
    print(user_in_db)
    # usuario no está registrado en la base de datos
    if not user_in_db:
        flash("Invalid Email/Password","error")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # si obtenemos False después de verificar la contraseña
        flash("Invalid Email/Password","error")
        return redirect('/')
    # si las contraseñas coinciden, configuramos el user_id en sesión
    session['user_id'] = user_in_db.id
    return redirect("/recipes")

@app.route('/logout')
def logout():
    session.clear()
    return redirect("/")
