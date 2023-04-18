from typing import List

from api.planetscale_connection import get_db_session, Session

from db.seeding.course_data_seeder import seed_course_data, parse_args, get_sections_from_args
from db.seeding.static_data_seeder import seed_static_data

from courses_data.data_extractor import Section


def seed(session: Session, sections: List[Section]):
    print("\n> Starting DB Seeding procedure...")
    seed_static_data(session)
    seed_course_data(session, sections)
    

def main():
    args = parse_args()
    sections = get_sections_from_args(args)
    
    session = get_db_session(autocommit=False)
    seed(session, sections)
    session.close()
    
    
if __name__ == '__main__':
    main()
