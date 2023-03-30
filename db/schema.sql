/* 
	Database for CourseMate 
    Sprint 3 
*/

drop database if exists course_mate;
create database if not exists course_mate;
use course_mate;

CREATE TABLE subject(
	code VARCHAR(4) NOT NULL,
    name VARCHAR(64),
    
	PRIMARY KEY (code),
    
    UNIQUE(name)
);

CREATE TABLE major(
	id SMALLINT NOT NULL AUTO_INCREMENT,
    level VARCHAR(3) NOT NULL,
	name VARCHAR(64) NOT NULL,
    
    PRIMARY KEY (id),
    
    UNIQUE(level, name)
);

CREATE TABLE account(
	id INT NOT NULL AUTO_INCREMENT,
	email_address VARCHAR(320) NOT NULL, 
    edu_email_address VARCHAR(320),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    phone_number VARCHAR(15),
    grad_year YEAR NOT NULL,
    major_id SMALLINT NOT NULL,
    
	PRIMARY KEY (id),
    FOREIGN KEY (major_id) REFERENCES major(id)
); 

CREATE TABLE friendship(
	account_id_1 INT NOT NULL,
    account_id_2 INT NOT NULL,
    status ENUM('pending', 'accepted') NOT NULL,
    
    PRIMARY KEY (account_id_1, account_id_2),
	FOREIGN KEY (account_id_1) REFERENCES account(id) ON DELETE CASCADE,
    FOREIGN KEY (account_id_2) REFERENCES account(id) ON DELETE CASCADE
); 

CREATE TABLE semester(
	id SMALLINT NOT NULL AUTO_INCREMENT,
    term ENUM('fall', 'spring', 'summer') NOT NULL,
    semester_year YEAR NOT NULL,
    
    PRIMARY KEY (id),
    
    UNIQUE(term, semester_year)
);

CREATE TABLE class(
	id INT NOT NULL AUTO_INCREMENT,
    subject_code VARCHAR(4) NOT NULL,
	class_number VARCHAR(5) NOT NULL,
    name varchar(100),
    description TEXT,
    
    PRIMARY KEY (id)
); 

CREATE TABLE instructor(
	id INT NOT NULL AUTO_INCREMENT,
	first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    
    PRIMARY KEY (id)
);

CREATE TABLE location(
	id INT NOT NULL AUTO_INCREMENT,
	building VARCHAR(80) NOT NULL,
    room VARCHAR(50) NOT NULL,
    
    PRIMARY KEY (id),
    
    UNIQUE(building, room)
);

CREATE TABLE section(
	id INT NOT NULL AUTO_INCREMENT,
	semester_id SMALLINT NOT NULL,
    class_id INT NOT NULL,
    crn INT NOT NULL,
    section_name VARCHAR(6) NOT NULL,
    instructors TEXT,
    times TEXT,
    location_id INT,
    
    PRIMARY KEY (id),
    FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE,
    FOREIGN KEY (semester_id) REFERENCES semester(id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES location(id),
    
    UNIQUE(semester_id, crn)
); 

CREATE TABLE section_instructor(
	section_id INT NOT NULL,
    instructor_id INT NOT NULL,
    
	PRIMARY KEY (section_id, instructor_id),
    FOREIGN KEY (section_id) REFERENCES section(id) ON DELETE CASCADE,
    FOREIGN KEY (instructor_id) REFERENCES instructor(id) ON DELETE CASCADE
);

CREATE TABLE schedule(
	account_id INT NOT NULL,
    section_id INT NOT NULL,
    
    PRIMARY KEY (account_id, section_id),
    FOREIGN KEY (account_id) REFERENCES account(id) ON DELETE CASCADE,
    FOREIGN KEY (section_id) REFERENCES section(id) ON DELETE CASCADE
); 


