from sqlalchemy import Table, MetaData
from sqlalchemy.engine.reflection import Inspector

from api.planetscale_connection import Session


def get_table_from_db(session: Session, table: Table):
    table_name = table.__tablename__
    metadata = MetaData()
    metadata.reflect(bind=session.get_bind())
    db_table = Table(table_name, metadata)
    return db_table


def delete_all_entries_in_table(session: Session, table: Table):
    db_table = get_table_from_db(session, table)
    delete_stmt = db_table.delete()
    session.execute(delete_stmt)
    session.commit()
    
    
def create_table(session: Session, table: Table):
    table.metadata.create_all(session.get_bind())
    session.commit()
    
    
def drop_table(session: Session, table: Table):
    db_table = get_table_from_db(session, table)
    db_table.drop(session.get_bind())
    session.commit()
    

def drop_table_if_exists(session: Session, table: Table):
    inspector = Inspector.from_engine(session.get_bind())
    if inspector.has_table(table.__tablename__):
        drop_table(session, table)