# -*- coding:utf-8 -*-
import weatherdaemon
import os
global mainarg
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
config=weatherdaemon.Config("config.ini")

#Creating database session
SQLALCHEMY_DATABASE_URI = config.DBengine+"://" + config.DBuser + ':' + config.DBpassword + '@' + config.DBserver + '/'+ config.DBname
engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
#/Creating database session

def clrscr():
    try:
        os.system('clear')
    except:
        os.system('cls')
        
def MainMenu():
    clrscr()
    arg=-1
    print("\t       WeatherDaemon main console        ")   
    print("\t#########################################")
    print("\t#       1) Citiess                       #")
    print("\t#       2) Regions                      #")
    print("\t#       3) Countries                    #")
    print("\t#       4) VK groups                    #")
    print("\t#       5) Export tables                #")
    print("\t#       6) Backup                       #")
    print("\t#       7) About                        #")
    print("\t#########################################")
    arg = int(input("Select: "))

    if arg==1:
        Cities()
    else:
            if arg==2:
                Regions()
            else:
                if arg==3:
                    Countries()
                else:
                    if arg==4:
                        VKGroups()
                    else:
                        if arg==5:
                            Export()
                        else:
                            if arg==6:
                                BackUP()
                            else:
                                if arg==7:
                                    AboutT()
        

def Cities():
    clrscr()
    arg=-1
    print("\t             Cities console              ")
    print("\t#########################################")
    print("\t#       1) Add                          #")
    print("\t#       2) Edit                         #")
    print("\t#       3) Erase                        #")
    print("\t#       4) View                         #")
    print("\t#########################################")
    arg = int(input("Select: "))
    
    if arg==1:
        AddCity()
    else:
        if arg==2:
            EditCity()
        else:
            if arg==3:
                EraseCity()
            else:
                if arg==4:
                    ViewCity() 

                                        
def Regions():
    clrscr()
    print("\t            Regions console              ")
    print("\t#########################################")
    print("\t#       1) Add                          #")
    print("\t#       2) Edit                         #")
    print("\t#       3) Erase                        #")
    print("\t#       4) View                         #")
    print("\t#########################################")
    arg = int(input("Select: "))

    if arg==1:
        AddRegion()
    else:
        if arg==2:
            EditRegion()
        else:
            if arg==3:
                EraseRegion()
            else:
                if arg==4:
                    ViewRegion()
    
def Countries():
    clrscr()
    print("\t           Countries console             ")
    print("\t#########################################")
    print("\t#       1) Add                          #")
    print("\t#       2) Edit                         #")
    print("\t#       3) Erase                        #")
    print("\t#       4) View                         #")
    print("\t#########################################")
    arg = int(input("Select: "))

    if arg==1:
        AddCountry()
    else:
        if arg==2:
            EditCountry()
        else:
            if arg==3:
                EraseCountry()
            else:
                if arg==4:
                    ViewCountry()  
def VKGroups():
    clrscr()
    print("\t             VK Groups console           ")
    print("\t#########################################")
    print("\t#       1) Add                          #")
    print("\t#       2) Edit                         #")
    print("\t#       3) Erase                        #")
    print("\t#       4) View                         #")
    print("\t#########################################")
    arg = int(input("Select: "))

    if arg==1:
        AddVKGroup()
    else:
        if arg==2:
            EditVKGroup()
        else:
            if arg==3:
                EraseVKGroup()
            else:
                if arg==4:
                    ViewVKGroup()
                        
def Export():
    clrscr()
    print("\t             Export console              ")
    print("\t#########################################")
    print("\t#       1) Forecast to XML              #")
    print("\t#       2) Forecast to XLS              #")
    print("\t#       3) Forecast to MXL              #")
    print("\t#########################################")
    arg = int(input("Select: "))

    if arg==1:
        ForecastToXML()
    else:
        if arg==2:
            ForecastToXLS()
        else:
            if arg==3:
                ForecastToMXL()


def BackUP():
    clrscr()
    print("\t             BackUP console              ")
    print("\t#########################################")
    print("\t#       1) Full BackUP                  #")
    print("\t#########################################")
    arg = int(input("Select: "))

    if arg==1:
        FullBackUP()
        

def AboutT():
    clrscr()
    AboutText = '''WeatherDaemon (c) 2013-2016
Многострочного
Текста'''
    print(AboutText)

def AddCity():
    clrscr()
    City = weatherdaemon.City()
    clrscr()
    print("You input this city")
    print(City)
    confirm = input("Do you want to add this city to db? y/n:")
    if confirm == "y":
        session.add(City)
    else:
        input("City not added.")
        AddCity()

    
def EditCity():
    print("EditCity")
    
def EraseCity():
    print("EraseCity")
    
def ViewCity():
    print("ViewCity")
    
def AddRegion():
    print("AddRegion")
    
def EditRegion():
    print("EditRegion")
    
def EraseRegion():
    print("EraseRegion")
    
def ViewRegion():
    print("ViewRegion")
    
def AddCountry():
    print("AddCountry")
    
def EditCountry():
    print("EditCountry")
    
def EraseCountry():
    print("EraseCountry")
    
def ViewCountry():
    print("ViewCountry")
    
def AddVKGroup():
    print("AddVKGroup")
    
def EditVKGroup():
    print("EditVKGroup")
    
def EraseVKGroup():
    print("EraseVKGroup")
    
def ViewVKGroup():
    print("ViewVKGroup")
    
def ForecastToXML():
    print("ForecastToXML")
    
def ForecastToXLS():
    print("ForecastToXLS")
    
def ForecastToMXL():
    print("ForecastToMXL")
    
def FullBackUP():
    print("FullBackUP")
    

MainMenu()

session.commit()   #end session