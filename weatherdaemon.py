# -*- coding:utf-8 -*-
import sys
import sqlalchemy
import string
from xml.dom.minidom import parse

def getConfig():
	global dbUser, dbPassword, dbName, tabPrefix
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
	

def InitialiseDataBase():
	print("1) MySQL", "2) PgSQL", sep='\n')
	DBtype = raw_input("Select db type: ")
	DBserver = raw_input("Database server IP or name")
	DBport = raw_input("")
	DBuser = raw_input("")
	DBpassword = raw_input("")
	DBname = raw_input("")
	
	
def addCity():
	ZIPCODE = raw_input("City ZIP code: ")
	LATINNAME = raw_input("Latin City Name: ")
	RUSNAME = raw_input("Russian City Name: ")
	YANDEX = raw_input("Yandex Weather Code: ")
	GISMETEO = raw_input("Gismeteo Weather Code: ")
	VKID = raw_input("VK Group: ")
	