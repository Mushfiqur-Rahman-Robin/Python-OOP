from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] = 'ba84590ac747e1f1617d9f2cd88d93c3' 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'   # /// means relative path for sqlite from the current file
db = SQLAlchemy(app) 

from flaskblog import routes