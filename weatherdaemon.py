# -*- coding:utf-8 -*-
import sys
import sqlalchemy
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
	
	data=XMLconf.getElementsByTagName('dbCitiesName')
	for e in data:
		for t in e.childNodes:
			dbCitiesName = t.data
	
	data=XMLconf.getElementsByTagName('tabPrefix')
	for e in data:
		for t in e.childNodes:
			dbWeatherName = t.data

def DoQuery(qhost, quser, qpassword, qdb, qsql):
	
	
def addCity()
	ZIPCODE = raw_input("City ZIP code: ")
	LATINNAME = raw_input("Latin City Name: ")
	RUSNAME = raw_input("Russian City Name: ")
	YANDEX = raw_input("Yandex Weather Code: ")
	GISMETEO = raw_input("Gismeteo Weather Code: ")
	VKID = raw_input("VK Group: ")