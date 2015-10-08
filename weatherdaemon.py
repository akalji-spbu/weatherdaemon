# -*- coding:utf-8 -*-
import sys
import MySQLdb
import string
from xml.dom.minidom import parse

def getConfig():
	global dbCitiesUser, dbCitiesPassword, dbCitiesName, dbWeatherUser, dbWeatherPassword, dbWeatherName, tabPrefix
	XMLconf=parse("config.xml")
	data=XMLconf.getElementsByTagName('dbUser')
	for e in data:
		for t in e.childNodes:
			dbCitiesUser = t.data
			
	data=XMLconf.getElementsByTagName('dbPassword')
	for e in data:
		for t in e.childNodes:
			dbCitiesPassword = t.data
	
	data=XMLconf.getElementsByTagName('dbName')
	for e in data:
		for t in e.childNodes:
			dbCitiesName = t.data
	
	data=XMLconf.getElementsByTagName('tabPrefix')
	for e in data:
		for t in e.childNodes:
			dbWeatherName = t.data

def DoQuery(qhost, quser, qpassword, qdb, qsql):
	db = MySQLdb.connect(host=qhost, user=quser, passwd=qpassword, db=qdb, use_unicode = 1, charset='utf8')
	db.set_character_set('utf8')
	Cursor=db.cursor()
	Cursor.execute('SET NAMES utf8')
	Cursor.execute('SET CHARACTER SET utf8')
	Cursor.execute('SET character_set_connection=utf8')
	Cursor.execute(qsql)
	dbCities.commit()
	dbCities.close()
	
def addCity()
	ZIPCODE = raw_input("City ZIP code: ")
	LATINNAME = raw_input("Latin City Name: ")
	RUSNAME = raw_input("Russian City Name: ")
	YANDEX = raw_input("Yandex Weather Code: ")
	GISMETEO = raw_input("Gismeteo Weather Code: ")
	VKID = raw_input("VK Group: ")