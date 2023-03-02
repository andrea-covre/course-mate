use course_mate;

-- init all the UG Majors
INSERT INTO major (level, name, code) 
VALUES 
('BS', 'Aerospace Engineering', 'AE'),
('BS', 'Applied Languages and Intercultural Studies', null),
('BS', 'Architecture', 'ARCH'),
('BS', 'Applied Physics', null),
('BS', 'Biochemistry', null),
('BS', 'Biology', 'BIOL'),
('BS', 'Biomedical Engineering', 'BMED'),
('BS', 'Building Construction', 'BC'),
('BS', 'Business Administration', null),
('BS', 'Chemical and Biomolecular Engineering', 'CHBE'),
('BS', 'Chemistry', 'CHEM'),
('BS', 'Civil Engineering', 'CEE'),
('BS', 'Computational Media', null),
('BS', 'Computer Engineering', 'ECE'),
('BS', 'Computer Science', 'CS'),
('BS', 'Earth and Atmospheric Sciences', 'EAS'),
('BS', 'Economics', 'ECON'),
('BS', 'Economics and International Affairs'),
('BS', 'Electrical Engineering', 'EE'),
('BS', 'Environmental Engineering', null),
('BS', 'Global Economics and Modern Languages', null),
('BS', 'History, Technology, and Society', 'HTS'),
('BS', 'Industrial Design', 'ID'),
('BS', 'Industrial Engineering', 'ISYE'),
('BS', 'International Affairs', 'INTA'),
('BS', 'International Affairs and Modern Languages', null),
('BS', 'Literature, Media, and Communication', 'LMC'),
('BS', 'Materials Science and Engineering', 'MSE'),
('BS', 'Mathematics', 'MATH'),
('BS', 'Mechanical Engineering', 'ME'),
('BS', 'Music Technology', null),
('BS', 'Neuroscience', 'NEUR'),
('BS', 'Nuclear and Radiological Engineering', 'NRE'),
('BS', 'Physics', 'PHYS'),
('BS', 'Psychology', 'PYSC'),
('BS', 'Public Policy', 'PUBP');


/* Might init these values from the OSCAR Crawler directly
INSERT INTO subject (subject_code) 
VALUES 
('ACCT'), ('AE'), ('AAPH'), ('ARCH'), ('BS'), ('BIO'), ('BMED'), ('CEE'), ('CETL'), ('CHBE'), ('CHEM'),
('CHIN'), ('COA'), ('COE'), ('CS'), ('DAT'), ('EAS'), ('ECE'), ('ECON'), ('ENGL'), ('FREN'), ('GRMN'),
('GT'), ('HIST'), ('ID'), ('INTA'), ('ISYE'), ('KOR'), ('LING'), ('LMC'), ('MATH'), ('MCAT'), ('ME'),
('MGT'), ('MSE'), ('MUSI'), ('NRE'), ('PHIL'), ('PHYS'), ('POL'), ('PSYC'), ('PTFE'), ('PUBP'), ('SOC'),
('SAPN');
*/