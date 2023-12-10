from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql
SQLALCHEMY_DATABASE_URI = "sqlite:///example.db"

# engine = create_engine("mssql://scott:tiger@hostname:port/dbname")
host = "127.0.0.1"         
user = "root"          
passwd = "root"    
database = "foo"     

# Database connection
db=pymysql.connect(
        host=host,
        user=user,
        passwd=passwd,
        db=database,
        autocommit=True)

engine = create_engine(f'mysql+pymysql://{user}:{passwd}@{host}/{database}')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

