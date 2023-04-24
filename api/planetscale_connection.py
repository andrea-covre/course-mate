from dotenv import load_dotenv
import os
import MySQLdb
import sqlalchemy as db

from sqlalchemy.orm import Session

def get_db_session(autocommit=True):
    load_dotenv()
    connection = MySQLdb.connect(
    host= os.getenv("HOST"),
    user=os.getenv("USERNAME"),
    passwd= os.getenv("PASSWORD"),
    db= os.getenv("DATABASE"),
    ssl_mode = "VERIFY_IDENTITY",
    ssl      = {
        "ca": os.getenv("SSL_CA")
    }
    )

    engine = db.create_engine('mysql+mysqldb://', creator=lambda: connection)
    
    if autocommit:
        engine = engine.execution_options(isolation_level="AUTOCOMMIT")
        
    session = Session(engine)
    return session