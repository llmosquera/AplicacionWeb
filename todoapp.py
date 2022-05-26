#Importar la flask 
#from urllib import request
from operator import index, cur 
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
 #Ejecutar la conexión 
 
app = Flask(__name__)
#mysql conexion 
app.config['MYSQL_HOST']= 'localhost'
app.config['MYSQL_USER']= ''
app.config['MYSQL_PASSWORD']= ''
app.config['MYSQL_DB']= 'flask-web'
mysql = MySQL(app)

app.secret_key= 'mysecretkey'

@app.route('/')
def Index():
    mysql.connection.cursor()
    cur.execute('SELECT * FROM insertar')
    data = cur.fetchall()
    return render_template('index.html', insertar = data)

@app.route('/insertar', methods=['POST'])
def insertar():
    if request.method == 'POST':
      Tarea = request.form['Tarea']
      Email = request.form['Email']
      Prioridad = request.form['Prioridad']
      cur = mysql.connection.cursor()
      cur.execute('INSERT INTO insertar (Tarea, Email, Prioridad) VALUES (%s, %s, %s)',
      (Tarea, Email, Prioridad))
      mysql.connection.commit()
      flash('contacto agregado ')
      return redirect(url_for('Index'))

@app.route('/Editar')
def Editar_insertar():
    return 'Editar insertar'

@app.route('/Guardar')
def Guardar_insertar():
    return 'Guardar insertar'
 
@app.route('/Eliminar/<string:id>')
def Eliminar_insertar(id):
    return print 
 #Ejecutar el servidor 
if __name__=='__main__':
   app.run(port = 3000, debug = True)