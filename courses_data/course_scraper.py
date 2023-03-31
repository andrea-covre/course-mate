import pickle
import argparse
import requests
from time import time
from bs4 import BeautifulSoup

from courses_data.data_extractor import extract_data, SEMESTER_TO_MONTH

URL = 'https://oscar.gatech.edu/bprod/bwckschd.p_get_crse_unsec'

HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://oscar.gatech.edu',
        'Accept-Language': 'en-US,en;q=0.9',
        'Host': 'oscar.gatech.edu',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.15',
        'Referer': 'https://oscar.gatech.edu/bprod/bwckgens.p_proc_term_date',
        'Connection': 'keep-alive',
    }

BASE_DATA = [
    ('sel_subj', 'dummy'),
    ('sel_day', 'dummy'),
    ('sel_schd', 'dummy'),
    ('sel_insm', 'dummy'),
    ('sel_camp', 'dummy'),
    ('sel_levl', 'dummy'),
    ('sel_sess', 'dummy'),
    ('sel_instr', 'dummy'),
    ('sel_ptrm', 'dummy'),
    ('sel_attr', 'dummy'),
    ('sel_crse', ''),
    ('sel_title', ''),
    ('sel_schd', '%'),
    ('sel_from_cred', ''),
    ('sel_to_cred', ''),
    ('sel_camp', '%'),
    ('sel_ptrm', '%'),
    ('sel_instr', '%'),
    ('sel_attr', '%'),
    ('begin_hh', '0'),
    ('begin_mi', '0'),
    ('begin_ap', 'a'),
    ('end_hh', '0'),
    ('end_mi', '0'),
    ('end_ap', 'a'),
]

SUBJECTS_LIST = [
    'ACCT', 'AE', 'AS', 'APPH', 'ASE', 'ARBC', 'ARCH', 'BIOS', 'BIOL', 'BMEJ', 'BMED', 
    'BMEM', 'BCP', 'BC', 'CETL', 'CHBE', 'CHEM', 'CHIN', 'CP', 'CEE', 'COA', 'COE', 'CX', 
    'CSE', 'CS', 'COOP', 'UCGA', 'EAS', 'ECON', 'ECEP', 'ECE', 'ENGL', 'FS', 'FREN', 
    'GT', 'GTL', 'GRMN', 'GMC', 'HS', 'HIST', 'HTS', 'ISYE', 'ID', 'INTA', 'IL', 'INTN', 
    'IMBA', 'JAPN', 'KOR', 'LS', 'LING', 'LMC', 'MGT', 'MOT', 'MLDR', 'MSE', 'MATH', 'ME', 
    'MP', 'MSL', 'ML', 'MUSI', 'NS', 'NEUR', 'NRE', 'PHIL', 'PHYS', 'POL', 'PTFE', 'PSYC', 'PUBP', 
    'PUBJ', 'RUSS', 'SOC', 'SPAN', 'SWAH', 'VIP', 'WOLO'
    ]


def parse_args():
    # create the parser object
    parser = argparse.ArgumentParser(description='Accepts a year and a semester')

    # add arguments
    parser.add_argument('semester', choices=['fall', 'summer', 'spring'], help='the semester (fall, summer, or spring)')
    parser.add_argument('year', type=int, help='the year (e.g. 2023)')

    # parse the arguments
    args = parser.parse_args()
    
    return args


def get_request_data_body(year: int, semester: str):
    data = BASE_DATA
    
    # Get term code
    term = f"{year}{SEMESTER_TO_MONTH[semester]:02d}"
    
    # Add term information to the data of the request
    data.append(('term_in', term))
    
    # Add all subjects to the data of the request
    requested_subjects = []
    for subject in SUBJECTS_LIST:
        requested_subjects.append(('sel_subj', subject))
        
    data.extend(requested_subjects)
    
    return data


def scrape_course_data(year: int, semester: str):
    data_body = get_request_data_body(year, semester)

    print(f"> Requesting OSCAR for the {semester.capitalize()} {year} semester course data...")
    response = requests.post(URL, headers=HEADERS, data=data_body)

    print(f"> Status code: {response.status_code}")
    
    if response.status_code != 200:
        print("Error: Could not get the data")
        return

    print("> Extracting data from the response...")
    html = BeautifulSoup(response.content, "html.parser")
    html = str(html)
    
    sections = extract_data(html)
    
    output_filename = f"{semester}_{year}_{int(time())}.pkl"
    print(f"\n> Saving sections data to {output_filename}")
    with open(output_filename, 'wb') as f:
        pickle.dump(sections, f)
        
    return sections
    
def main():
    args = parse_args()
    year = args.year
    semester = args.semester
    
    print("\n\t >> Starting OSCAR Scraping procedure <<")
    scrape_course_data(year, semester)
    

if __name__ == '__main__':
    main()