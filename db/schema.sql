/* 
	Database for CourseMate 
    Sprint 3 
*/

drop database if exists course_mate;
create database if not exists course_mate;
use course_mate;

CREATE TABLE account(
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

CREATE TABLE friendship(
	account_id_1 INT NOT NULL,
    account_id_2 INT NOT NULL,
    status ENUM('pending', 'accepted') NOT NULL,
    
    PRIMARY KEY (account_id_1, account_id_2),
	FOREIGN KEY (account_id_1) REFERENCES account(id) ON DELETE CASCADE,
    FOREIGN KEY (account_id_2) REFERENCES account(id) ON DELETE CASCADE
); 

CREATE TABLE subject(
	id INT NOT NULL AUTO_INCREMENT,
	subject_code VARCHAR(4),
    
    PRIMARY KEY (id),
    
    UNIQUE(subject_code)
);

CREATE TABLE major(
	id INT NOT NULL AUTO_INCREMENT,
    level VARCHAR(3) NOT NULL,
	name VARCHAR(64) NOT NULL,
    code VARCHAR(4),
    
    PRIMARY KEY (id),
    
    UNIQUE(level, name),
    UNIQUE(level, code)
);

CREATE TABLE class(
	id INT NOT NULL AUTO_INCREMENT,
	term ENUM('fall', 'spring', 'summer') NOT NULL,
    year_ YEAR NOT NULL,
    subject_code VARCHAR(4) NOT NULL,
	class_number SMALLINT NOT NULL,
    name varchar(100),
    description TEXT,
    
    PRIMARY KEY (id),
    FOREIGN KEY (subject_code) REFERENCES subject(subject_code)
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
	class_id INT NOT NULL,
    crn INT NOT NULL,
    section_name VARCHAR(6) NOT NULL,
    instructors TEXT,
    times TEXT,
    location_id INT,
    seats SMALLINT,
    
    PRIMARY KEY (class_id),
    FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE,
    FOREIGN KEY (location_id) REFERENCES location(id),
    
    UNIQUE(class_id, crn)
); 

CREATE TABLE schedule(
	account_id INT NOT NULL,
	class_id INT NOT NULL,
    crn INT NOT NULL,
    
    PRIMARY KEY (account_id, class_id, crn),
    FOREIGN KEY (account_id) REFERENCES account(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id) REFERENCES class(id) ON DELETE CASCADE,
    FOREIGN KEY (class_id, crn) REFERENCES section(class_id, crn) ON DELETE CASCADE
); 


