from sqlalchemy import Table, MetaData

from api.planetscale_connection import Session

def delete_all_entries_in_table(session: Session, table_name: str):
    metadata = MetaData()
    metadata.reflect(bind=session.get_bind())
    table = Table(table_name, metadata, autoload=True)
    delete_stmt = table.delete()
    session.execute(delete_stmt)
    session.commit()