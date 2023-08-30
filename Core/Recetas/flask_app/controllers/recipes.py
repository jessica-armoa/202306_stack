from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app.models.recipe import Recipe
from flask_app import app

@app.route("/recipes")
def home():
    if not session.get('user_id'):
        return redirect("/")

    user_in_session=User.get_by_id(session['user_id'])
    recipes=Recipe.get_all()
    users=User.get_all()

    print("USER ID IN SESION", user_in_session.id)

    print("ALL RECIPES")
    for recipe in recipes:
        print(recipe.id, recipe.name, recipe.user_id)

    print("ALL USERS")
    for user in users:
        print(user.id,user.first_name)

    dict_users = {}
    for user in users:
        dict_users[user.id] = user

    return render_template("home.html", user_in_session=user_in_session, recipes=recipes, users=dict_users)

@app.route("/recipes/new")
def new_recipe():
    if not session.get('user_id'):
        return redirect("/")

    return render_template("new_recipe.html")

@app.route("/recipes/new/process", methods=['POST'])
def new_recipe_process():
    if not session['user_id']:
        return redirect("/")

    print("NEW RECIPE:::::",request.form)
    recipe_data = {
                "name" : request.form["name"],
                "description" : request.form["description"],
                "instructions" : request.form["instructions"],
                "date_coocked" : request.form["date_coocked"],
                "under_30" : bool(request.form["under_30"]),
                "user_id" : session["user_id"],
            }
    Recipe.save(recipe_data)
    return redirect('/recipes')

@app.route("/recipes/<id>")
def view_recipe(id):
    if not session.get('user_id'):
        return redirect("/")

    recipe = Recipe.get_by_id(id)
    user_in_session=User.get_by_id(session['user_id'])
    users=User.get_all()
    dict_users = {}
    for user in users:
        dict_users[user.id] = user
    return render_template("view_recipe.html",recipe=recipe, user_in_session=user_in_session, users=dict_users)

@app.route("/recipes/edit/<id>")
def edit_recipe(id):
    if not session.get('user_id'):
        return redirect("/")

    recipe = Recipe.get_by_id(id)
    print("RECIPE NAME",recipe.name)
    return render_template("edit_recipe.html",recipe=recipe)

@app.route("/recipes/edit/<id>/process", methods=['POST'])
def edit_recipe_process(id):
    if not session.get('user_id'):
        return redirect("/")

    print(request.form)
    recipe_ = Recipe.get_by_id(id)
    recipe_data = {
                "id" : recipe_.id,
                "name" : request.form["name"],
                "description" : request.form["description"],
                "instructions" : request.form["instructions"],
                "date_coocked" : request.form["date_coocked"],
                "under_30" : bool(request.form["under_30"]),
                "user_id" : session["user_id"],
                "created_at" : recipe_.created_at
            }
    Recipe(recipe_data).edit()
    return redirect('/recipes')

@app.route("/recipes/delete/<id>")
def delete(id):
    if not session.get('user_id'):
        return redirect("/")

    recipe = Recipe.get_by_id(id)
    print("recipe a eliminar: ", recipe.id)
    recipe.delete()
    return redirect('/recipes')