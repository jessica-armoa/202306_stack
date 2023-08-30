from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask import flash

from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_db').query_db(query)
        print(results)
        # crear una lista vacía para agregar nuestras instancias de users
        users = []
        # Iterar sobre los resultados de la base de datos y crear instancias de users con cls
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_by_email(cls, email):
        data = {'email' : email}
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL('users_db').query_db(query,data)
        print(results[0])
        if results:
            return cls(results[0])
        return None

    @classmethod
    def get_by_id(cls, id):
        data = {'id' : id}
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL('users_db').query_db(query,data)
        print(results[0])
        if results:
            return cls(results[0])
        return None

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW());"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('users_db').query_db( query, data )

    @staticmethod
    def validate_user(data):
        is_valid = True
        if not data['first_name'].isalpha():
            flash("First name must have only letters","error")
            is_valid = False
        if len(data['first_name']) < 2:
            flash("First name must be at least 2 characters.","error")
            is_valid = False

        if not data['last_name'].isalpha():
            flash("Last name must have only letters","error")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("Last name must be at least 2 characters.","error")
            is_valid = False

        if not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!","error")
            is_valid = False
        if User.get_by_email(data['email']):
            flash("Email address already exists","error")
            is_valid = False

        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.","error")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Passwords are not the same","error")
            is_valid = False

        return is_valid