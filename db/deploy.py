from typing import List

from api.planetscale_connection import get_db_session, Session

from db.create_tables import create_all_tables
from db.seeding.full_seeder import seed
from db.seeding.course_data_seeder import parse_args, get_sections_from_args

from courses_data.data_extractor import Section


def deploy(session: Session, sections: List[Section]):
    print("\n\t >> Starting DB Deployment procedure <<")
    create_all_tables(session)
    seed(session, sections)
    print("\n\t >> DB Fully Deployed <<")
    

def main():
    args = parse_args()
    sections = get_sections_from_args(args)
    
    session = get_db_session()
    deploy(session, sections)
    session.close()
    
    
if __name__ == '__main__':
    main()