import re
import pickle
import argparse
from typing import List

from tqdm import tqdm

from api.planetscale_connection import get_db_session, Session
from api.models.semester import Semester
from api.models.instructor import Instructor
from api.models.section_instructor import Section_Instructor
from api.models.class_ import Class
from api.models.location import Location
from api.models.section import Section as SectionModel

from courses_data.data_extractor import Section, MONTH_TO_SEMESTER
from courses_data.course_scraper import scrape_course_data

from db.utils import delete_all_entries_in_table


def parse_args():
    parser = argparse.ArgumentParser(description='Seed the database with course data from either a file or from OSCAR directly')

    group = parser.add_mutually_exclusive_group(required=True)
    
    group.add_argument('--oscar', nargs=2, metavar=('SEMESTER', 'YEAR'),
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
    
    
def insert_semesters(session: Session, semesters: list):
    print(f"\n> Seeding DB with {len(semesters)} semesters...")
    for semester in tqdm(semesters):
        id = semester
        semester = str(semester)
        term = int(semester[-2:])
        year = int(semester[:-2])
        new_entry = {
            "id": id,
            "term": MONTH_TO_SEMESTER[term],
            "year": year
        }
        session.add(Semester(new_entry))
    session.commit()
    
def insert_instructors(session: Session, instructors: list):
    print(f"\n> Seeding DB with {len(instructors)} instructors...")
    batch_size = 400
    for idx, instructor in tqdm(enumerate(instructors), total=len(instructors)):
        first_name, middle_name, last_name = get_instructor_names(instructor)
        new_entry = {
            "first_name": first_name,
            "middle_name": middle_name,
            "last_name": last_name,
        }
        session.add(Instructor(new_entry))
        
        if idx % batch_size == 0:
            session.commit()
            
    session.commit()
        
        
def insert_classes(session: Session, classes: list):
    print(f"\n> Seeding DB with {len(classes)} classes...")
    # Using enumerate to commit to the database every batch_size entries
    batch_size = 400
    for idx, class_ in tqdm(enumerate(classes), total=len(classes)):
        subject, class_code = class_
        title = classes[class_]
        if len(title) > 1:
            title = "N/A"
        else:
            title = title[0]
            
        new_entry = {
            "subject_code": subject,
            "class_code": class_code,
            "title": title,
        }
        session.add(Class(new_entry))
        
        if idx % batch_size == 0:
            session.commit()
            
    session.commit()
        
        
def insert_locations(session: Session, locations: list):
    print(f"\n> Seeding DB with {len(locations)} locations...")
    for location in tqdm(locations):
        building, room = get_location_info(location)
        new_entry = {
            "building": building,
            "room": room,
        }
        session.add(Location(new_entry))
    session.commit()
    
    
def insert_section_instructor_relationship(session: Session, section: Section):
    if not section.instructors:
        return
    
    for instructor in section.instructors:
        first, middle, last = get_instructor_names(instructor)
        instructor_id = session.query(Instructor.id).filter_by(
                first_name=first, 
                middle_name=middle,
                last_name=last
            ).scalar()
        
        new_entry = {
            "section_id": section.section_id,
            "instructor_id": instructor_id
        }
        
        session.add(Section_Instructor(new_entry))
        

def insert_sections(session: Session, sections: list):
    print(f"\n> Seeding DB with {len(sections)} sections...")
    batch_size = 50
    for idx, section in tqdm(enumerate(sections), total=len(sections)):
        
        class_id = session.query(Class.id).filter_by(
                subject_code=section.subject, 
                class_code=section.class_code
            ).scalar()
        
        building, room = get_location_info(section.location)
        location_id = session.query(Location.id).filter_by(
                building=building, 
                room=room
            ).scalar()

        new_entry = {
            "section_id": section.section_id,
            "title": section.name,
            "semester_id": section.semester,
            "class_id": class_id,
            "crn": section.crn,
            "section_code": section.section_code,
            "days": section.days,
            "times": section.time,
            "location_id": location_id,
            "credits": section.credits,
            "description": section.description,
            "levels": section.levels,
            "grade_basis": section.grade_basis,
            "attributes": section.attributes,
            "campus": section.campus,
        }
        
        session.add(SectionModel(new_entry))
        insert_section_instructor_relationship(session, section)
        
        if idx % batch_size == 0:
            session.commit()
            
    session.commit()
        
def seed_course_data(session: Session, sections: List[Section]):
    """
    Seed the database with the unique semesters, instructors, classes, and locations
    """
    semesters, instructors, classes, locations = get_unique_semesters_instructors_classes_locations(sections)
    
    delete_all_entries_in_table(session, Semester)
    insert_semesters(session, semesters)
        
    delete_all_entries_in_table(session, Instructor)
    insert_instructors(session, instructors)
    
    delete_all_entries_in_table(session, Class)
    insert_classes(session, classes)
    
    delete_all_entries_in_table(session, Location)
    insert_locations(session, locations)
    
    delete_all_entries_in_table(session, SectionModel)
    delete_all_entries_in_table(session, Section_Instructor)
    insert_sections(session, sections)
    
    
def get_sections_from_args(args: argparse.Namespace) -> List[Section]:
    """
    Get the sections from the command line arguments
    """
    if args.oscar:
        semester, year = args.oscar
        sections = scrape_course_data(year, semester)
        
    elif args.file:
        filepath = args.file
        with open(filepath, "rb") as f:
            sections = pickle.load(f)
            
    return sections


def main():
    args = parse_args()
    sections = get_sections_from_args(args)
        
    # Create a session to the database
    session = get_db_session()
        
    # Seed the database with the unique semesters, instructors, classes, and locations
    seed_course_data(session, sections)

    session.close()

if __name__ == '__main__':
    main()