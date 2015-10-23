# -*- coding:utf-8 -*-
import sys
import sqlalchemy
import string
import config
from xml.dom.minidom import parse
 
class City():
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
        
    def saveCityToDB():
        print ("Hello")
        
        


class Forecast():
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
    
global CurrentConfig
CurrentConfig = Config()
