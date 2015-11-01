# -*- coding:utf-8 -*-
import sys
import string
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
        
    def __init__(self, CityCode = 0, EnglishName = 0, LocalName = 0, ZipCode = 0, RegionCode = 0, CountryCode = 0, Resort = 0):
        if CityCode==0:
            self.CityCode       = input("International Weather Code: ") 
            self.EnglishName    = input("City Name in English: ")
            self.LocalName      = input("City Name in National Language: ")
            self.ZipCode        = input("City ZIP code: ")
            self.RegionCode     = input("City Region code: ")
            self.CountryCode    = input("City Country code: ")
            self.Resort         = input("City resort status (true or false): ")
        else:
            self.CityCode       = CityCode
            self.EnglishName    = EnglishName 
            self.LocalName      = LocalName
            self.ZipCode        = ZipCode
            self.RegionCode     = RegionCode
            self.CountryCode    = CountryCode
            self.Resort         = Resort



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

#end core classes

#begin setup fucntions
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
            print("1) MySQL", "2) PgSQL", sep='\t')
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
                    raise SystemExit("Database successful initialised!")
                    
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
