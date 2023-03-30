import re
import pickle
import argparse
from typing import List

from tqdm import tqdm
from sqlalchemy import Table, MetaData

from api.planetscale_connection import get_db_session, Session
from api.models.semester import Semester
from api.models.instructor import Instructor
from api.models.class_ import Class
from api.models.location import Location

from courses_data.data_extractor import Section
from courses_data.course_scraper import scrape_course_data


INSTRUCTOR_TABLE_NAME = "instructor"
SEMESTER_TABLE_NAME = "semester"
CLASS_TABLE_NAME = "class"
LOCATION_TABLE_NAME = "location"


def parse_args():
    parser = argparse.ArgumentParser(description='Prime the database with course data from either a file or from OSCAR directly')

    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument('--semester', nargs=2, metavar=('SEMESTER', 'YEAR'),
                        help='Semester and year (e.g., Spring 2023)')
    
    group.add_argument('--file', metavar='FILEPATH',
                        help='Path to file')

    args = parser.parse_args()

    return args


def only_letters(s):
    return bool(re.match('^[a-zA-Z]+$', s))


def contains_digit(s):
    return bool(re.search('\d', s))


def is_valid_room(room: str):
    return not only_letters(room) and contains_digit(room)


def get_unique_semesters_instructors_classes_locations(sections: List[Section]): 
    semesters = set()
    instructors = set()
    locations = set()
    classes = dict()

    print(f"\n> Extracting unique semesters, instructors, classes, and locations from {len(sections)} sections...")
    for section in tqdm(sections):
        semesters.add(section.semester)
        locations.add(section.location)
        
        if section.instructors is not None:
            for instructor in section.instructors:
                instructors.add(instructor)
                
        subject = section.subject
        class_code = section.class_code
        
        if (subject, class_code) in classes:
            if section.name not in classes[(subject, class_code)]:
                classes[(subject, class_code)].append(section.name)
        else:
            classes[(subject, class_code)] = [section.name]
        
    return semesters, instructors, classes, locations


def get_instructor_names(instructor: str):
    names = instructor.split(" ")
    middle_name = None
    if len(names) == 2:
        first_name, last_name = names
        
    elif len(names) == 3:
        first_name, middle_name, last_name = names
        
    else:
        first_name = names[0]
        middle_name = " ".join(names[1:-1])
        last_name = names[-1]
        
    first_name = first_name.strip()
    last_name = last_name.strip()
    if middle_name:
        middle_name = middle_name.strip()
        
    return first_name, middle_name, last_name


def get_location_info(location: str):
    if not location:
        return "N/A", "N/A"
    
    if location == "TBA":
        return "TBA", "TBA"
    
    building = " ".join(location.split(" ")[:-1]).strip()
    room = location.split(" ")[-1].strip()
    
    if not is_valid_room(room):
        building += f" {room}"
        room = "N/A"
        
    return building, room


def delete_all_entries_in_table(session: Session, table_name: str):
    metadata = MetaData()
    metadata.reflect(bind=session.get_bind())
    table = Table(table_name, metadata, autoload=True)
    delete_stmt = table.delete()
    session.execute(delete_stmt)
    session.commit()
    
    
def insert_semesters(session: Session, semesters: list):
    for semester in tqdm(semesters):
        term, year = semester.split(" ")
        new_entry = {
            "term": term.strip(),
            "semester_year": int(year.strip())
        }
        session.add(Semester(new_entry))
    session.commit()
    
def insert_instructors(session: Session, instructors: list):
    for instructor in tqdm(instructors):
        first_name, middle_name, last_name = get_instructor_names(instructor)
        new_entry = {
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
        }
        session.add(Instructor(new_entry))
        session.commit()
        
        
def insert_classes(session: Session, classes: list):
    for class_ in tqdm(classes):
        subject, class_code = class_
        title = classes[class_]
        if len(title) > 1:
            title = "N/A"
        else:
            title = title[0]
            
        new_entry = {
            "subject_code": subject,
            "class_number": class_code,
            "name": title,
        }
        session.add(Class(new_entry))
        session.commit()
        
        
def insert_locations(session: Session, locations: list):
    for location in tqdm(locations):
        building, room = get_location_info(location)
        new_entry = {
            "building": building,
            "room": room,
        }
        session.add(Location(new_entry))
        session.commit()

def main():
    args = parse_args()
    
    sections: List[Section]
    if args.semester:
        semester, year = args.semester
        sections = scrape_course_data(year, semester)
        
    elif args.file:
        filepath = args.file
        with open(filepath, "rb") as f:
            sections = pickle.load(f)
        
    # Create a session to the database
    session = get_db_session()
        
    semesters, instructors, classes, locations = get_unique_semesters_instructors_classes_locations(sections)
        
    #Prime the database with the unique semesters, instructors, classes, and locations
    
    print(f"\n> Priming DB with {len(semesters)} semesters...")
    delete_all_entries_in_table(session, SEMESTER_TABLE_NAME)
    insert_semesters(session, semesters)
        
    print(f"\n> Priming DB with {len(instructors)} instructors...")
    delete_all_entries_in_table(session, INSTRUCTOR_TABLE_NAME)
    insert_instructors(session, instructors)
    
    print(f"\n> Priming DB with {len(classes)} classes...")
    delete_all_entries_in_table(session, CLASS_TABLE_NAME)
    insert_classes(session, classes)
    
    print(f"\n> Priming DB with {len(locations)} locations...")
    delete_all_entries_in_table(session, LOCATION_TABLE_NAME)
    insert_locations(session, locations)

    session.close()

if __name__ == '__main__':
    main()