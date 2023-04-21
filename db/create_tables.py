from tqdm import tqdm

from api.models.account import Account
from api.models.class_ import Class
from api.models.friendship import Friendship
from api.models.instructor import Instructor
from api.models.location import Location
from api.models.major import Major
from api.models.schedule import Schedule
from api.models.section_instructor import Section_Instructor
from api.models.semester import Semester
from api.models.subject import Subject
from api.models.section import Section
from api.planetscale_connection import get_db_session, Session

from db.utils import drop_table_if_exists, create_table, confirm


ALL_TABLES = [
    Account,
    # Class,
    # Friendship,
    # Instructor,
    # Location,
    # Major,
    # Schedule,
    # Section_Instructor,
    # Semester,
    # Subject,
    # Section
]


def create_all_tables(session: Session):
    print(f"\n> Creating {len(ALL_TABLES)} tables...")
    for table in tqdm(ALL_TABLES):
        drop_table_if_exists(session, table)
        create_table(session, table)


def main():
    print("This script will delete all the following tables in the database and recreate them:")
    for table in ALL_TABLES:
        print(f" - {table.__tablename__}")
        
    if not confirm('Are you sure you want to continue?', False):
        print("Aborting...")
        exit(0)
    
    session = get_db_session(autocommit=False)
    create_all_tables(session)
    session.close()


if __name__ == '__main__':
    main()
