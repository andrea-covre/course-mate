from dotenv import load_dotenv
import os
import MySQLdb
import sqlalchemy as db

from sqlalchemy.orm import Session
from sqlalchemy import select
from models.major import Major

def get_db_session():
    load_dotenv()
    connection = MySQLdb.connect(
    host= os.getenv("HOST"),
    user=os.getenv("USERNAME"),
    passwd= os.getenv("PASSWORD"),
    db= os.getenv("DATABASE"),
    ssl_mode = "VERIFY_IDENTITY",
    ssl      = {
        "ca": "/etc/ssl/cert.pem"
    }
    )

    engine = db.create_engine('mysql+mysqldb://', creator=lambda: connection)
    session = Session(engine)
    return session