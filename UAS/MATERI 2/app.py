"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

import os
import sys
import bottle
import sqlite3
from bottle import default_app, redirect, route, template, static_file, run, debug



if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    bottle.debug(True)
    

@route('/main')
def greet():
    return template('webUtama.html') 

@route('/')
def tttt():
    return template('index.tpl') 

@route('/cekDB') #MELIHAT DATABASE
def showDB():
    conn = sqlite3.connect('cars515.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cars515")
    result = c.fetchall()
    c.close()
# note: the SQL results are an array of data (tuple)
# send results as a string
    return str(result)

@route('/add')
def tambah():
    conn = sqlite3.connect('cars515.db')
    c = conn.cursor()
    c.execute("""INSERT INTO cars515 (ID, BRAND, MODEL, PRICE) VALUES ("123", "Toyota", "Fortuner TRD", "400")""")
    conn.commit()
    c.close()
    return'Berhasil Menambah Data'

@route('/update')
def tambah():
    conn = sqlite3.connect('cars515.db')
    c = conn.cursor()
    c.execute("""UPDATE cars515 SET PRICE='375' WHERE BRAND='Toyota' """)
    conn.commit()
    c.close()
    return'Berhasil Mengubah Data'

@route('/delete')
def tambah():
    conn = sqlite3.connect('cars515.db')
    c = conn.cursor()
    c.execute("""DELETE FROM cars515 WHERE ID='123'""")
    conn.commit()
    c.close()
    return'Berhasil Menghapus Data'

    
@bottle.route('/css/<filename:re:.*\.css>')
def send_css(filename):
    return static_file(filename, root='./css')

@bottle.route('/css/<filename:re:.*\.jpg>')
def send_jpg(filename):
    return static_file(filename, root='./css')

@bottle.route('/db/<filename:re:.*\.xml>')
def send_xml(filename):
    return static_file(filename, root='./db')
@bottle.route('/db/<filename:re:.*\.JSON>')
def send_json(filename):
    return static_file(filename, root='./db')
@bottle.route('/db/<filename:re:.*\.csv>')
def send_csv(filename):
    return static_file(filename, root='./db')



@bottle.route('/<filename:re:.*\.db>')
def send_csv(filename):
    return static_file(filename, root='./db')

def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return default_app()

if __name__ == '__main__':
    run(debug=True, reloader=True)
    # Starts a local test server.
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    
    bottle.run(server='wsgiref', host='localhost', port=PORT)
