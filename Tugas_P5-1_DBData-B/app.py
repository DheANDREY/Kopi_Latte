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
    

@route('/')
def greet():
    return template('webUtama.html') 

@route('/showDB')
def tttt():
    return template('dbMenu.tpl') 

@route('/cekDB') #MELIHAT DATABASE
def showDB():
    conn = sqlite3.connect('cars51.db')
    c = conn.cursor()
    c.execute("SELECT * FROM cars51")
    result = c.fetchall()
    c.close()
# note: the SQL results are an array of data (tuple)
# send results as a string
    return str(result)

@route('/add')
def tambah():
    conn = sqlite3.connect('cars51.db')
    c = conn.cursor()
    c.execute("""INSERT INTO cars51 (ID, BRAND, MODEL, PRICE) VALUES ("150", "DAIHATSU", "GRANMAX", "130")""")
    conn.commit()
    c.close()
    return'Berhasil Menambah Data'

@route('/update')
def tambah():
    conn = sqlite3.connect('cars51.db')
    c = conn.cursor()
    c.execute("""UPDATE cars51 SET MODEL='Crv' WHERE BRAND='HONDA' """)
    conn.commit()
    c.close()
    return'Berhasil Mengubah Data'

@route('/delete')
def tambah():
    conn = sqlite3.connect('cars51.db')
    c = conn.cursor()
    c.execute("""DELETE FROM cars51 WHERE ID='150'""")
    conn.commit()
    c.close()
    return'Berhasil Menghapus Data'

@route('/add2')
def addNEW():
    return template('form.tpl') + \
    print("New Post:", request.body.read()) 
    nid = request.forms.get("nid")
    nbrand = request.forms.get("nbrand")
    nmodel = request.forms.get("nmodel")
    nprice = request.forms.get("nprice")
    if nid != "":        
        conn = sqlite3.connect('cars51.db')
        c = conn.cursor()
        c.execute("""INSERT INTO cars51 (ID, BRAND, MODEL, PRICE) VALUES (nid, nbrand, nmodel, nprice)""")
        conn.commit()
        c.close()
    redirect("/p") # go back to the main page 

@route('/json')
def show_json():
    return '<h1> Ini Halaman menampilkan data .json</h1>' + template('db/Cars.json')

@route('/xml')
def show_xml():
    return '<h1> Ini Halaman menampilkan data .xml</h1>' + template('db/Cars.xml') 

@route('/csv')
def show_csv():
    return '<h1> Ini Halaman menampilkan data .csv</h1>' + template('db/Cars.csv')
    
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
    # Starts a local test server.
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    
    bottle.run(server='wsgiref', host='localhost', port=PORT)
