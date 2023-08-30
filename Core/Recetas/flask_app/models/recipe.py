from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_coocked = data['date_coocked']
        self.under_30 = bool(data['under_30'])
        self.created_at = data['created_at']
        self.user_id = data['user_id']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL('recipes_db').query_db(query)
        print(results)
        # crear una lista vacía para agregar nuestras instancias de users
        recipes = []
        # Iterar sobre los resultados de la base de datos y crear instancias de users con cls
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes

    @classmethod
    def get_user_with_recipes(cls):
        query = "SELECT * FROM users LEFT JOIN recipes ON recipes.user_id = users.id;"
        results = connectToMySQL('recipes_db').query_db(query)
        print("RESULTADOS",results)
        user = cls(results[0])
        # Iterar sobre los resultados de la base de datos y crear instancias
        for row in results:
            recipe_data = {
                "id" : row["recipes.id"],
                "name" : row["name"],
                "description" : row["description"],
                "instructions" : row["instructions"],
                "date_coocked" : row["date_coocked"],
                "under_30" : row["under_30"],
                "created_at" : row["created_at"]
            }
            user.recipes.append(Recipe(recipe_data))
        for n in user.recipes:
            print(n.id)
        return user

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO recipes (name, description, instructions, date_coocked, under_30, user_id, created_at) VALUES ( %(name)s, %(description)s, %(instructions)s, %(date_coocked)s, %(under_30)s, %(user_id)s, NOW());"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('recipes_db').query_db( query, data )

    @classmethod
    def get_by_id(cls,id):
        data = {"id" : id}
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL('recipes_db').query_db(query, data)
        print("RESULTS:",results)
        if results:
            return cls(results[0])
        return None

    def delete(self):
        data = {"id" : self.id}
        query = "DELETE FROM recipes WHERE id =  %(id)s;"
        connectToMySQL('recipes_db').query_db(query, data)
        return True

    def edit(self):
        data = {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "instructions" : self.instructions,
            "date_coocked" : self.date_coocked,
            "under_30" : self.under_30
        }
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instructions = %(instructions)s, date_coocked = %(date_coocked)s, under_30 = %(under_30)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL('recipes_db').query_db(query, data)
        return True

    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3 or len(data['description']) < 3 or len(data['instructions']) < 3:
            flash("name, description or instructions must be at least 3 characters.","error")
            is_valid = False

        return is_valid
