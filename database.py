from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
##Explanation Needed
DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(DATABASE_URL)
Sessionlocal = sessionmaker(autoflush=False,autocommit = False,bind=engine)
Base = declarative_base()####in form of tables