from flask import Flask
import sqlite3
app = Flask(__name__)
app.config.from_object('settings')

from home import views