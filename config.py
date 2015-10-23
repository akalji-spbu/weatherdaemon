dbServer = 'localhost'
dbUser = 'weatherdaemon'
dbPassword = 'weaterdaemon'  
dbName = 'weatherdaemon'  
tabPrefix  = 'wdae_' 

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' +dbUser+ ':' +dbPassword+ '@' +dbServer+ '/'+ dbName
engine = sqlalchemy.create_engine(SQLALCHEMY_DATABASE_URI, echo=True)