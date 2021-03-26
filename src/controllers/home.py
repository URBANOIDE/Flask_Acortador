from flask import render_template, request, redirect, url_for
from src import app
import random
from random import choice
from src.models.acortador import AcortadorUrl

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
       return render_template('index.html')
    
    url_original = request.form.get('acortar')

    #Url local
    url_local = "http://127.0.0.1:5000/"
   
    #cantidad de caracateres que tomara en el recorrido del for
    longitud = 4
    
    #caracteres a seleccionar aleaotorios
    caracter = "abcdefghijklmñopqrstuvwxyz1234567890"
    
    #4 caracteres aleatorios
    url_corta = url_local + ''.join(random.choice(caracter) for i in range(longitud))

    #concat url local y url corta
    #url_final = url_local + url_corta

    acortadorUrl = AcortadorUrl()
    acortadorUrl.insertar(url_original, url_corta)

    #me redirecciona a la misma pagina pero esta vez con la url cargada en la vista
    return render_template('index.html', url_corta = url_corta)

