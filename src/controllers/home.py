from flask import render_template, request, redirect, url_for, Flask, session
from src import app
import random
from random import choice
from src.models.acortador import AcortadorUrl
import hashlib


@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
       return render_template('index.html')
    
    #url a guardar en db como url_original
    url_original = request.form.get('acortar')

    #Url local
    url_local = "http://127.0.0.1:5000/"
   
    #cantidad de caracateres que tomara en el recorrido del for
    longitud = 4
    
    #caracteres a seleccionar aleaotorios
    caracter = "abcdefghijklmñopqrstuvwxyz1234567890"
    url_corta = ""
    #4 caracteres aleatorios, guardar en bd como url_corta
    url_corta = url_corta.join(random.choice(caracter) for i in range(longitud))

   #url a mostrar al usuario
    url_mostrar =url_local + url_corta

          
    
    acortadorUrl = AcortadorUrl()
    acortadorUrl.insertar(url_original, url_corta)

    #me redirecciona a la misma pagina pero esta vez con la url cargada en la vista
   
    return render_template('index.html', url_mostrar = url_mostrar)
@app.route('/user', methods =['GET', 'POST'])
def index_user():
    if request.method == 'GET':
       return render_template('index.html')
    
    #url a guardar en db como url_original
    url_original = request.form.get('acortar')

    #Url local
    url_local = "http://127.0.0.1:5000/"
   
    #cantidad de caracateres que tomara en el recorrido del for
    longitud = 4
    
    #caracteres a seleccionar aleaotorios
    caracter = "abcdefghijklmñopqrstuvwxyz1234567890"
    url_corta = ""
    #4 caracteres aleatorios, guardar en bd como url_corta
    url_corta = url_corta.join(random.choice(caracter) for i in range(longitud))

   #url a mostrar al usuario
    url_mostrar =url_local + url_corta

    id = session['id']

          
    
    acortadorUrl = AcortadorUrl()
    acortadorUrl.insertar_user(id, url_original, url_corta)

    #me redirecciona a la misma pagina pero esta vez con la url cargada en la vista
   
    return render_template('index.html', url_mostrar = url_mostrar)


#redireccion
@app.route('/<url_corta>', methods =['GET', 'POST'])
def redireccionar(url_corta):
   acortadorUrl = AcortadorUrl()
   links = acortadorUrl.redirigir(url_corta)
   return redirect(links[2])





#registar usuarios
@app.route('/registro', methods =['GET', 'POST'])
def registrar_usuario():
  if request.method == 'GET':
     return render_template('registro.html')
  nombre = request.form.get('nombre')
  email = request.form.get('email')
  password = request.form.get('password')
   #encriptar contraseña
  #h = hashlib.sha1('sha1', password.encode('utf8'))

  acortadorUrl = AcortadorUrl()
  acortadorUrl.registrar(nombre, email, password)

  return render_template('index.html')





@app.route('/entrar', methods =['GET', 'POST'])
def login():
  if request.method == 'GET':
   return render_template('inicio.html')
  email = request.form.get('email')
  password = request.form.get('password')


  
  acortadorUrl = AcortadorUrl()
  user = acortadorUrl.iniciar(email, password)
  #mensaje para alerta de error de ingreso
  error = "Error de ingreso"
  #sesiones
  session['usuario'] = user[1]
  session['id'] = user[0]

  #validacion de ingreso
  if user != None:
     return render_template('indexuser.html')
  else: return render_template('inicio.html', error = error)

##cerrar cesion
@app.route('/cerrar')
def logout():
   session.pop('usuario', None)
   session.pop('id', None)

   return redirect(url_for('index'))



