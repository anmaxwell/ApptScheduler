import os
from flask import Flask

app = Flask(__name__)

#adding security to prevent XS forgery attacks etc.
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#to prevent getting stuck in circular imports create this last
from scheduler import routes, models