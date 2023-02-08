from flask import Flask
from config import config
from flask_mysqldb import MySQL
app = Flask(__name__)

app.config['SECRET_KEY'] = config['SECRET_KEY'] 
app.config['MYSQL_HOST'] = config['DATABASE_HOST']
app.config['MYSQL_DB'] = config['DATABSE_NAME']
app.config['MYSQL_USER'] = config['DATABASE_USER']
app.config['MYSQL_PASSWORD'] = config['DATABASE_PASSWORD']

mysql = MySQL(app)

from simple_flask_api import routes