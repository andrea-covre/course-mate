from api.queries import Database
from api.planetscale_connection import get_db_session

__session = get_db_session(autocommit=True)
db = Database(__session)