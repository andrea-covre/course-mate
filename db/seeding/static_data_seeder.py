from tqdm import tqdm

from api.planetscale_connection import get_db_session, Session
from api.models.major import Major
from api.models.subject import Subject

from db.utils import delete_all_entries_in_table

from static_data.majors_list import ALL_MAJORS
from static_data.subject_codes import SUBJECT_CODES


def insert_subjects(session: Session):
    print(f"\n> Seeding DB with {len(SUBJECT_CODES)} subjects...")
    for subject in tqdm(SUBJECT_CODES):
        code, name = subject
        new_entry = {
            "code": code,
            "name": name
        }
        session.add(Subject(new_entry))
        session.commit()
        
        
def insert_majors(session: Session):
    print(f"\n> Seeding DB with {len(ALL_MAJORS)} majors...")
    for major in tqdm(ALL_MAJORS):
        level, name = major
        new_entry = {
            "level": level,
            "name": name
        }
        session.add(Major(new_entry))
        session.commit()


def seed_static_data(session: Session):
    """
    Seed the database with the static data (majors, subjects, etc.)
    """
    delete_all_entries_in_table(session, Subject)
    insert_subjects(session)
    
    delete_all_entries_in_table(session, Major)
    insert_majors(session)
    

def main():
    session = get_db_session(autocommit=False)
    seed_static_data(session)
    session.close()

if __name__ == '__main__':
    main()