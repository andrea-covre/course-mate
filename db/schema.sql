/* Database for CourseMate Sprint 3 */

drop database if exists course_mate;
create database if not exists course_mate;
use course_mate;

Create table ACCOUNTS(
	id INT NOT NULL AUTO_INCREMENT,
	email_address VARCHAR(320) NOT NULL, 
    edu_email_address VARCHAR(320),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15),
    grad_year YEAR NOT NULL,
    major ENUM('Computer Science', 'Mathematics', 'Biology') NOT NULL,
    
	PRIMARY KEY (id)
); 

Create table FRIENDSHIPS(
	account_id_1 INT NOT NULL,
    account_id_2 INT NOT NULL,
    status ENUM('pending', 'accepted') NOT NULL,
    
    PRIMARY KEY (account_id_1, account_id_2),
	FOREIGN KEY (account_id_1) REFERENCES ACCOUNTS(id) ON DELETE CASCADE,
    FOREIGN KEY (account_id_2) REFERENCES ACCOUNTS(id) ON DELETE CASCADE
); 

Create table CLASSES(
	id INT NOT NULL AUTO_INCREMENT,
	term ENUM('fall', 'spring', 'summer') NOT NULL,
    year_ YEAR NOT NULL,
    subject ENUM('ACCT', 'AE', 'AAPH', 'ARCH', 'BS', 'BIO', 'BMED', 'CEE', 'CETL', 'CHBE', 
		'CHEM', 'CHIN', 'COA', 'COE', 'CS', 'DAT', 'EAS', 'ECE', 'ECON', 'ENGL', 'FREN', 'GRMN', 'GT',
        'HIST', 'ID', 'INTA', 'ISYE', 'KOR', 'LING', 'LMC', 'MATH', 'MCAT', 'ME', 'MGT', 'MSE', 'MUSI', 'NRE', 'PHIL', 'PHYS', 'POL', 'PSYC', 'PTFE', 'PUBP', 'SOC', 'SPAN') NOT NULL,
	class_number SMALLINT NOT NULL,
    description TEXT,
    
    PRIMARY KEY (id)
); 

Create table SECTIONS(
	class_id INT NOT NULL,
    crn INT NOT NULL,
    section_name VARCHAR(6) NOT NULL,
    instructors TEXT,
    times TEXT,
    location TEXT,
    seats SMALLINT,
    
    PRIMARY KEY (class_id),
    FOREIGN KEY (class_id) REFERENCES CLASSES(id) ON DELETE CASCADE,
    
    UNIQUE(class_id, crn)
); 

Create table SCHEDULES(
	account_id INT NOT NULL,
	class_id INT NOT NULL,
    crn INT NOT NULL,
    
    PRIMARY KEY (account_id, class_id, crn),
    FOREIGN KEY (account_id) REFERENCES ACCOUNTS(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES CLASSES(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id, crn) REFERENCES SECTIONS(class_id, crn) ON DELETE CASCADE
); 

Create table MAJORS(
	id INT NOT NULL,
	major_name VARCHAR(64),
    subject_code INT,
    
    PRIMARY KEY (id),
    
    UNIQUE(major_name),
    UNIQUE(subject_code)
);

Create table SUBJECTS(
	id INT NOT NULL,
	subject_code VARCHAR(4),
    linked_major INT,
    
    PRIMARY KEY (id),
    
    UNIQUE(subject_code),
    UNIQUE(linked_major)
);
