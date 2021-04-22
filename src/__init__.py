from flask import Flask, render_template

app = Flask(__name__, template_folder= 'views')
app.secret_key = "my_secrret_key"
#importar los controllers
from src.controllers import *

def create_app():
    app.run(debug=True, port=5000)
