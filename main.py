from flask import Flask, render_template,redirect, url_for, request, session
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from pprint import pprint
import hashlib
import time
import mysql.connector
import itertools

mydb = mysql.connector.connect (	
	host = "localhost",
	user = "root",
	password = "",
	database = "raspored"
)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

	
@app.route('/raspored')
def raspored():
	mc = mydb.cursor()

	
	#mc.execute("SELECT * FROM raspored WHERE nastavnik LIKE "+input.search)
	
	mc.execute("SELECT * FROM raspored")
	res = mc.fetchall()
	mc2 = mydb.cursor()
	mc2.execute("SELECT DISTINCT nastavnik from raspored")
	#mc.execute("SELECT nastavnik, COUNT(nastavnik) FROM raspored GROUP BY nastavnik HAVING COUNT(nastavnik) > 1") 
	nastavnici = mc2.fetchall()
	mc3 = mydb.cursor()
	mc3.execute("SELECT DISTINCT vreme from raspored")
	
	#mc.execute("SELECT vreme, COUNT(vreme) FROM raspored GROUP BY vreme HAVING COUNT(vreme) > 1")
	ucionice = mc3.fetchall()


	#data = [nastavnici] + [vreme]
	return render_template ("raspored.html", raspored=res, nastavnici=nastavnici, ucionice=ucionice)
	#return render_template("raspored.html",raspored=res, data=data)

@app.route ("/nastavnik/<indeks>")
def nastavnik(indeks):
	mc =mydb.cursor()
	mc.execute("SELECT * FROM raspored WHERE nastavnik='"+indeks+"'")
	res = mc.fetchall()
	mc2 = mydb.cursor()
	mc2.execute("SELECT DISTINCT nastavnik FROM raspored")
	nastavnici = mc2.fetchall()
	mc3 = mydb.cursor()
	mc3.execute("SELECT DISTINCT vreme FROM raspored")
	ucionice = mc3.fetchall()
	return render_template ("raspored.html", raspored=res, nastavnici=nastavnici, ucionice=ucionice)


@app.route ("/ucionica/<raf>")
def ucionica(raf):
	mc =mydb.cursor()
	mc.execute("SELECT * FROM raspored WHERE vreme='"+raf+"'")
	res = mc.fetchall()
	mc2 = mydb.cursor()
	mc2.execute("SELECT DISTINCT nastavnik FROM raspored")
	nastavnici = mc2.fetchall()
	mc3 = mydb.cursor()
	mc3.execute("SELECT DISTINCT vreme FROM raspored")
	ucionice = mc3.fetchall()
	return render_template ("raspored.html", raspored=res, nastavnici=nastavnici, ucionice=ucionice)




if __name__ == '__main__':
	app.run(debug=True)