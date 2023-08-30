from flask import Flask, request, render_template, redirect, url_for, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from models import createTables
from models import User, Todo
from models import db as db
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from auth import verifyToken
import jwt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:password@localhost:5432/postgres"
app.config['JWT_SECRET_KEY'] = "chavelindadagiovanna"
app.config['JWT_ALGORITHM'] = 'HS256'
db.init_app(app)

createTables(app)

@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login_user():
    userLogin = request.form['user']
    passwordLogin = request.form['password']

    user = User.query.filter_by(user=userLogin).first()

    if user and check_password_hash(user.password, passwordLogin):
        try:
            key = "chavelindadagiovanna"
            userToken = jwt.encode({"userId": str(user.id)}, key, algorithm="HS256")

            response = make_response(redirect(url_for('todo')))
            response.set_cookie('userId', str(user.id), httponly=True, secure=True)
            response.set_cookie('authToken', userToken, httponly=True, secure=True)

            return response

        except Exception as e:
                return {
                    "error": "Quebrou foi tudo",
                    "message": str(e)
                }, 500
    else:
        return "Credenciais inválidas", 401
    

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.form['user']
    password = request.form['password']
    
    if not User.query.filter_by(user=user).first():
    
        hashedPassword = generate_password_hash(password, method="pbkdf2")

        newUser = User(user=user, password=hashedPassword)
        db.session.add(newUser)
        db.session.commit()
        return redirect("http://localhost:5000/") 
    else:
        return "Invalid Credentials", 401


@app.route('/todo')
@verifyToken
def todo(currentUser):
    jsonify(currentUser)
    tasks = Todo.query.all()
    return render_template('todo.html', tasks=tasks)

@app.route('/add_todo', methods=['POST'])
def add_post():
    content = request.form['content']
    
    newTask = Todo(content=content)
    db.session.add(newTask)
    db.session.commit()
    
    return redirect(url_for('todo'))

@app.route('/add_todo_page')
@verifyToken
def postpublish(currentUser):
    jsonify(currentUser)
    return render_template('addTodo.html')

@app.route('/sign_out', methods=["GET"])
def signout():

    response = make_response(redirect('http://localhost:5000/'))
    response.delete_cookie('userId')
    response.delete_cookie('authToken')
    
    return response

app.run(debug=True)