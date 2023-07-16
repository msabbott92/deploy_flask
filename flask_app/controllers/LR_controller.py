from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt  
from flask_app.models.LR_model import User

bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/register/user', methods=['POST'])
def register():
    if not User.validate_user(request.form):
        return redirect("/")
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "fav_language": request.form['fav_language'],
        "email": request.form['email'],
        "password" : bcrypt.generate_password_hash(request.form['password'])
    }
    id = User.save(data)
    session['user_id'] = id
    return redirect("/")

@app.route('/login', methods=['POST'])
def login():
    data = { "email" : request.form["email"] }
    user = User.get_by_email(data)
    print(user)
    if not user:
        flash("Invalid Email/Password")
        return redirect("/")
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Email/Password")
        return redirect('/')
    session['user_id'] = user.id
    return redirect("/dashboard")

@app.route("/dashboard")
def dashboard():
    data = {
        "id": session['user_id']
    }
    return render_template("dashboard.html", user = User.get_one(data))

