from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#sql_db_url = 'postgresql://postgres:123321qwsaqwsa@localhost:5432/fastapi_edu.db'
sql_db_url = 'postgresql://postgres:123321qwsaqwsa@localhost:5432/testdb'

engine = create_engine(sql_db_url)

session_local = sessionmaker(bind = engine)

Base = declarative_base()
