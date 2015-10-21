# -*- coding:utf-8 -*-
import sys
import sqlalchemy
import string
from xml.dom.minidom import parse
	
class Config(object):
    def __init__(self, ConfigFile):
        XMLconf=parse("config.xml")
        data=XMLconf.getElementsByTagName('dbUser')
        for e in data:
            for t in e.childNodes:
                dbUser = t.data
        data=XMLconf.getElementsByTagName('dbPassword')
        for e in data:
            for t in e.childNodes:
                dbPassword = t.data
        data=XMLconf.getElementsByTagName('dbName')
        for e in data:
            for t in e.childNodes:
                dbName = t.data
        data=XMLconf.getElementsByTagName('tabPrefix')
        for e in data:
            for t in e.childNodes:
                dbName = t.data
        self.dbUser = dbUser
        self.dbPassword = dbPassword  
        self.dbName = dbName  
        self.tabPrefix  = tabPrefix  
    

class City(object):
    def __init__(self, EnglishName, LocalName, CityCode, ZIPcode, Country):
        self.EnglishName = EnglishName
        self.LocalName = LocalName
        self.CityCode = CityCode
        self.ZIPcode = ZIPcode
        self.Country = Country
    
    def createCity():
        self.EnglishName = raw_input("City Name in English: ")
        self.LocalName = raw_input("City Name in English: ")
        self.CityCode = raw_input("City weather code: ")
        self.ZIPcode = raw_input("City ZIP code: ")
        self.Country = raw_input("Country: ")


class Forecast(object):
    def __init__(self, CityCode, Date):
        self.Date = Date
def CreateWeatherPicture():
    return CreateWeatherPicture

def install():
	print("1) MySQL", "2) PgSQL", sep='\n')
	DBtype = raw_input("Select db type: ")
	DBserver = raw_input("Database server IP or name: ")
	DBport = raw_input("Database service port: ")
	DBuser = raw_input("DB username: ")
	DBpassword = raw_input("DB password: ")
	DBname = raw_input("Name of DB: ")