import os

config = {
    "SECRET_KEY" : os.urandom(32),
    "DATABASE_HOST" : "localhost",
    "DATABSE_NAME" : "first_flask_api",
    "DATABASE_USER" : "root",
    "DATABASE_PASSWORD" : "",
}