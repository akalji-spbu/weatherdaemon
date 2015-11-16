# -*- coding:utf-8 -*-
import sys
import string
from datetime import datetime
import configparser
from xml.dom.minidom import parse
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#begin core classes
class Config:
    def __init__(self, ConfigFile):
        try:
            f = open(ConfigFile, 'r');
        except FileNotFoundError:
            print("Config file doesn't exists. Do you want create new engine config?")
            cf = input("(yes/no)?: ")
            if cf == "yes":
                setup()
            else:
                Dead("user_inaction")
        else:
            f.close()
            Configure = configparser.ConfigParser()
            Configure.read(ConfigFile)
            self.DBengine   = Configure["DB"]["DBengine"]
            self.DBserver   = Configure["DB"]["DBserver"]
            self.DBport     = Configure["DB"]["DBport"]
            self.DBuser     = Configure["DB"]["DBuser"]
            self.DBpassword = Configure["DB"]["DBpassword"]
            self.DBname     = Configure["DB"]["DBname"]
            
            
class City(Base):
    __tablename__ = 'cities'
    CityCode    = Column(Integer, primary_key=True)
    EnglishName = Column(String(30))
    LocalName   = Column(String(30))
    ZipCode     = Column(Integer)
    RegionCode  = Column(Integer)
    CountryCode = Column(Integer)
    Resort      = Column(Integer)
    TimeZone    = Column(Integer)
        
    def __init__(self, CityCode = 0, EnglishName = 0, LocalName = 0, ZipCode = 0, RegionCode = 0, CountryCode = 0, Resort = 0, TimeZone = 0):
        if CityCode==0:
            self.CityCode       = input("International Weather Code: ") 
            self.EnglishName    = input("City Name in English: ")
            self.LocalName      = input("City Name in National Language: ")
            self.ZipCode        = input("City ZIP code: ")
            self.RegionCode     = input("City Region code: ")
            self.CountryCode    = input("City Country code: ")
            self.Resort         = input("City resort status (True or False): ")
            self.TimeZone       = input("Citi's timezone is (from -12 to +12): ")         
            #self.latitude, self.longitude = GetCoordinates()
        else:
            self.CityCode       = CityCode
            self.EnglishName    = EnglishName 
            self.LocalName      = LocalName
            self.ZipCode        = ZipCode
            self.RegionCode     = RegionCode
            self.CountryCode    = CountryCode
            self.Resort         = Resort
            self.TimeZone       = TimeZone
            #self.latitude, self.longitude = GetCoordinates()

    def __repr__(self):
        return "<City(CityCode='%s', EnglishName='%s', LocalName='%s', ZipCode='%s', RegionCode='%s', CountryCode='%s', Resort='%s', TimeZone='%s')>" % (self.CityCode, self.EnglishName, self.LocalName, self.ZipCode, self.RegionCode, self.CountryCode, self.Resort, self.TimeZone)
    

class Region(Base):
    __tablename__ = 'regions'
    RegionCode    = Column(Integer, primary_key=True)
    EnglishName   = Column(String(30))
    LocalName     = Column(String(30))
    CountryCode   = Column(String(30))
    
    def __init__(self, RegionCode =0, EnglishName = 0, LocalName = 0, CountryCode = 0):
        if RegionCode==0:
            self.RegionCode     = input("City Region code: ")
            self.EnglishName    = input("City Name in English: ")
            self.LocalName      = input("City Name in English: ")
            self.CountryCode    = input("City Country code: ")
        else:
            self.RegionCode     = RegionCode
            self.EnglishName    = EnglishName
            self.LocalName      = LocalName
            self.CountryCode    = CountryCode
    def __repr__(self):
        return "<Region(RegionCode='%s', EnglishName='%s', LocalName='%s', CountryCode='%s')>" % (self.RegionCode, self.EnglishName, self.LocalName, self.CountryCode)
    
   
    
class Country(Base):
    __tablename__ = 'countries'
    CountryCode   = Column(Integer, primary_key=True)
    EnglishName   = Column(String(30))
    LocalName     = Column(String(30))
    
    def __init__(self, CountryCode = 0, EnglishName = 0, LocalName = 0):
        if RegionCode==0:
            self.CountryCode    = input("City Country code: ")
            self.EnglishName    = input("City Name in English: ")
            self.LocalName      = input("City Name in English: ")
        else:
            self.CountryCode    = CountryCode
            self.EnglishName    = EnglishName
            self.LocalName      = LocalName
    def __repr__(self):
        return "<Country(CountryCode='%s', EnglishName='%s', LocalName='%s')>" % (self.CountryCode, self.EnglishName, self.LocalName)
    

class VK_g(Base):
    __tablename__ = 'vk_subs'
    sub_id        = Column(Integer, primary_key=True)
    CityCode      = Column(String(30))
    GroupID       = Column(String(30))
    Expired       = Column(Integer)
    APIkey        = Column(String(30))
    User          = Column(String(30))
    Password      = Column(String(30))
    
    def __init__(self, sub_id = 0, CityCode = 0, GroupID = 0, Expired = 0, APIkey = 0, User = 0, Password = 0):
        if RegionCode==0:
            self.CityCode   = input(": ")
            self.GroupID    = input(": ")
            self.Expired    = input(": ")
            self.APIkey     = input(": ")
            self.User       = input(": ")
            self.Password   = input(": ")
        else:
            self.CityCode   = CityCode
            self.GroupID    = GroupID
            self.Expired    = Expired
            self.APIkey     = APIkey
            self.User       = User
            self.Password   = Password
    
    
    def __repr__(self):
        return "<VK(sub_id='%s', CityCode='%s', GroupID='%s', Expired='%s', APIkey='%s', User='%s', Password='%s')>" % (self.sub_id, self.CityCode, self.GroupID, self.Expired, self.APIkey, self.User, self.Password)
            
class Forecast(Base):
    __tablename__   = 'forecast'
    Timestamp       = Column(Integer, primary_key=True)
    CityCode        = Column(Integer)
    Cloudiness      = Column(Integer)
    Precipitation   = Column(Integer)
    Rpower          = Column(Integer)
    Spower          = Column(Integer)
    Pressure        = Column(Integer)
    Tempirature     = Column(Integer)
    WindMin         = Column(Integer)
    WindMax         = Column(Integer)
    WindDirection   = Column(Integer)
    Relwet          = Column(Integer)
    Heat            = Column(Integer)
    Sunrise         = Column(Integer)
    Sunset          = Column(Integer)
    Moonrise        = Column(Integer)
    Moonset         = Column(Integer)
    Moonphase       = Column(Integer)
    
    def __init__(self, Timestamp = 0, CityCode = 0, Cloudiness = 0, Precipitation = 0, Rpower = 0, Spower = 0, Pressure = 0, Tempirature = 0, WindMin = 0, WindMax = 0, WindDirection = 0, Relwet = 0, Heat = 0, Sunrise = 0, Sunset = 0, Moonrise = 0, Moonset = 0, Moonphase = 0):
        if CityCode==0:
            self.Timestamp      = Timestamp
            self.CityCode       = CityCode
            self.Cloudiness     = Cloudiness
            self.Precipitation  = Precipitation
            self.Rpower         = Rpower
            self.Spower         = Spower
            self.Pressure       = Pressure
            self.Tempirature    = Tempirature
            self.WindMin        = WindMin
            self.WindMax        = WindMax
            self.WindDirection  = WindDirection
            self.Relwet         = Relwet
            self.Heat           = Heat
            self.Sunrise        = Sunrise
            self.Sunset         = Sunset
            self.Moonrise       = Moonrise
            self.Moonset        = Moonset
            self.Moonphase      = Moonphase
        else:
            self.Timestamp      = Timestamp()
            self.CityCode       = input(": ")
            self.Cloudiness     = input(": ")
            self.Rpower         = input(": ")
            self.Spower         = input(": ")
            self.Pressure       = input(": ")
            self.Tempirature    = input(": ")
            self.WindMin        = input(": ")
            self.WindMax        = input(": ")
            self.WindDirection  = input(": ")
            self.Relwet         = input(": ")
            self.Heat           = input(": ")
            self.Sunrise        = input(": ")
            self.Sunset         = input(": ")
            self.Moonrise       = input(": ")
            self.Moonset        = input(": ")
            self.Moonphase      = input(": ")

    
    def __repr__(self):
        return "<Forecast(Timestamp='%s', CityCode='%s', Cloudiness='%s', Precipitation='%s', Rpower='%s', Spower='%s', Pressure='%s', Tempirature='%s', WindMin='%s', WindMax='%s', WindDirection='%s', Relwet='%s', Heat='%s', Sunrise='%s', Sunset='%s', Moonrise='%s', Moonset='%s', Moonphase='%s')>" % (self.Timestamp, self.CityCode, self.Cloudiness, self.Precipitation, self.Rpower, self.Spower, self.Pressure, self.Tempirature, self.WindMin, self.WindMax, self.WindDirection, self.Relwet, self.Heat, self.Sunrise, self.Sunset, self.Moonrise, self.Moonset, self.Moonphase)

def setup():
    ConfigFile = "config.ini"
    try:
        f = open(ConfigFile, 'r');
    except FileNotFoundError:
        print("1) MySQL", "2) PgSQL", sep='\t')
        DBtype     = input("Select db type: ")
        DBserver   = input("Database server IP or name: ")
        DBport     = input("Database service port: ")
        DBuser     = input("DB username: ")
        DBpassword = input("DB password: ")
        DBname     = input("Name of DB: ")
    else:
        f.close()
        print("Configuration alredy exists, do you want replace it?")
        cf = input("(yes/no)?: ")
        if cf == "yes":
            print("1) MySQL", "2) PgSQL, 3) MSSQL", sep='\t')
            DBtype   = input("Select db type: ")
            DBserver   = input("Database server IP or name: ")
            DBport     = input("Database service port: ")
            DBuser     = input("DB username: ")
            DBpassword = input("DB password: ")
            DBname     = input("Name of DB: ")
        else:
            f.close()
            print("Do you want current configuration file initialise DB?")
            cf = input("(yes/no)?: ")
            if cf != "yes":
                Dead("user_inaction")
            else: 
                config = Config("config.ini")
                print("Trying to connect...")
                if TestConnection(config.DBengine,config.DBserver, config.DBport, config.DBuser, config.DBpassword, config.DBname):
                    print("Database alredy exists.")
                    initDB()
                raise Dead("Database successful initialised!")
                    
        if DBtype == 1:
            DBengine="mysql+pymysql://"
        if DBtype == 2:
            DBengine="postgresql+psycopg2://"

        if TestConnection(DBengine,DBserver, DBport, DBuser, DBpassword, DBname):
            config = configparser.ConfigParser()
            config['DB'] = {}
            config['DB']['DBengine']    = DBengine
            config['DB']['DBserver']    = DBserver
            config['DB']['DBport']      = DBport
            config['DB']['DBuser']      = DBuser
            config['DB']['DBpassword']  = DBpassword
            config['DB']['DBname']      = DBname
            with open(ConfigFile, 'w') as configfile:
                config.write(configfile)
            initDB()

def initDB():
    print("Initialising DB in progress....")
    config = Config("config.ini")
    SQLALCHEMY_DATABASE_URI = DBengine + DBuser + ':' + DBpassword + '@' + DBserver + '/'+ DBname
    Base = declarative_base()
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    
    
    
#end setup fucntions

def TestConnection(DBengine,DBserver, DBport, DBuser, DBpassword, DBname):
    SQLALCHEMY_DATABASE_URI = DBengine + DBuser + ':' + DBpassword + '@' + DBserver + '/'+ DBname
    try:
        engine      = create_engine(SQLALCHEMY_DATABASE_URI)
        connection  = engine.connect()
    except sqlalchemy.exc.OperationalError:
        print("Database doesn't exists or username/password incorrect")
        print("Do you want try again")
        cf = input("(yes/no)?: ")
        if cf == "yes":
            setup()
        else:
            Dead("user_inaction")
    else:
        connection.close()
        return True
    
def Dead(error_reason):
    if error_reason == "user_inaction":
        print("Your choice does not imply the further work program")
        print("Program terminate now")
        print("See you")
        raise SystemExit("error_reason")
    
    if error_reason == 0:   #Normal exit code
        print("Good Bye!")
    raise SystemExit("error_reason")

def GetOneWeather(CitiCode):
    Gismeteo    = ParseGismeteo(CitiCode)
    Yandex      = ParseYandex(CitiCode)
    Sunrise     = Sunrise(CitiCode)
    Sunset      = Sunset(CitiCode)
    Moonrise    = Moonrise(CitiCode)
    Moonset     = Moonset(CitiCode)
    Moonphase   = Moonphase(CitiCode)
    Weather     = Forecast(CityCode, (Gismeteo.Cloudiness+Yandex.Cloudiness)/2, (Gismeteo.Precipitation+Yandex.Precipitation)/2, (Gismeteo.Rpower+Yandex.Rpower)/2, (Spower.Cloudiness+Spower.Cloudiness)/2, (Gismeteo.Pressure+Yandex.Pressure)/2, (Gismeteo.Tempirature+Yandex.Tempirature)/2, (Gismeteo.WindMin+Yandex.WindMin)/2, (Gismeteo.WindMax+Yandex.WindMax)/2, (Gismeteo.WindDirection+Yandex.WindDirection)/2, (Gismeteo.Relwet+Yandex.Relwet)/2, (Gismeteo.Heat+Yandex.Heat)/2, Sunrise, Sunset, Moonrise, Moonset, Moonphase)    
    
def ParseGismeteo(CitiCode):
    URL = "http://informer.gismeteo.ru/xml/"+CitiCode+"_1.xml"
    
    Cloudiness
    Precipitation
    Rpower
    Spower
    Pressure
    Tempirature
    WindMin
    WindMax
    WindDirection
    Relwet
    Heat
    Sunrise = 0
    Sunset = 0
    Moonrise  = 0
    Moonset = 0
    Moonphase = 0
    Forecast = Forecast(Timestamp(), CityCode, Cloudiness, Precipitation, Rpower, Spower, Pressure, Tempirature, WindMin, WindMax, WindDirection, Relwet, Heat, Sunrise, Sunset, Moonrise, Moonset, Moonphase)
    return Forecast
    
def ParseYandex(CitiCode):
    URL = "https://export.yandex.ru/weather-ng/forecasts/"+CitiCode+".xml"
    
    Cloudiness
    Precipitation
    Rpower
    Spower
    Pressure
    Tempirature
    WindMin
    WindMax
    WindDirection
    Relwet
    Heat
    Sunrise = 0
    Sunset = 0
    Moonrise = 0
    Moonset = 0
    Moonphase = 0
    Forecast = Forecast(Timestamp(), CityCode, Cloudiness, Precipitation, Rpower, Spower, Pressure, Tempirature, WindMin, WindMax, WindDirection, Relwet, Heat, Sunrise, Sunset, Moonrise, Moonset, Moonphase)
    return Forecast

def Sunrise(CitiCode): 
    Sunrise = 0
    return Sunrise

def Sunset(CitiCode):
    Sunset = 0
    return Sunset

def Moonrise(CitiCode):
    Moonrise = 0
    return Moonrise

def Moonset(CitiCode): 
    Moonset = 0
    return Moonset

def Moonphase(CitiCode):
    Moonphase = 0
    return Moonphase

def ExportToXLS(Query, TableTuple, File):
    print("exportDone")


def ExportToMXL(Query, TableTuple, File):
    print("exportDone")

def ExportToXML(Query, TableTuple, File):
    print("exportDone")
    
def Timestamp():
    timestamp = 0
    return timestamp
def PostToVK(Image, VKID):
    print("exportDone")

def Logger():   #ассинхронная функция
    print("LoggingIsStarted")

def GenerateImage(Forecast)
    return Base64(Image)

def GetCoordinates()
    return latitude, longitude

def clrscr():
    try:
        os.system('clear')
    except:
        os.system('cls')