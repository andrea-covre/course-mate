use course_mate;

INSERT INTO major (level, name, code) 
VALUES 
-- init all the UG Majors
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
('BS', 'Economics and International Affairs', null),
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
('BS', 'Public Policy', 'PUBP'),

-- init all the GRAD Majors
('MS', 'Aerospace Engineering', 'AE'),
('MS', 'Analytics', null),
('MS', 'Applied Languages and Intercultural Studies', null),
('MS', 'Architecture', 'ARCH'),
('MS', 'Bioengineering', null),
('MS', 'Bioinformatics', null),
('MS', 'Biology', 'BIOL'),
('MS', 'Biomedical Engineering', 'BMED'),
('MS', 'Building Construction and Facility Managment', 'BC'),
('MS', 'Business Administration (MBA)', null),
('MS', 'Chemical and Biomolecular Engineering', 'CHBE'),
('MS', 'Chemical Engineering', null),
('MS', 'Chemistry', 'CHEM'),
('MS', 'Civil Engineering', 'CEE'),
('MS', 'City and Regional Planning & Civil Engineering', null),
('MS', 'Computational Media & Digital Media', null),
('MS', 'Computational Science and Engineering', 'CSE'),
('MS', 'Computer Science', 'CS'),
('MS', 'Cybersecurity', null),
('MS', 'Digital Media', null),
('MS', 'Earth and Atmospheric Sciences', 'EAS'),
('MS', 'Economics', 'ECON'),
('MS', 'Electrical Engineering', 'EE'),
('MS', 'Electrical and Computer Engineering', 'ECE'),
('MS', 'Engineering Science and Mechanics', null),
('MS', 'Environmental Engineering', null),
('MS', 'Geographic Information Science and Technology', null),
('MS', 'Global Development', null),
('MS', 'Global Media and Cultures', 'GMC'),
('MS', 'Health Systems', 'HS'),
('MS', 'History and Sociology of Technology and Science', null),
('MS', 'Human-Computer Interaction', 'HCI'),
('MS', 'Industrial Design', 'ID'),
('MS', 'Industrial Engineering', 'ISYE'),
('MS', 'International Affairs', 'INTA'),
('MS', 'International Logistics', 'IL'),
('MS', 'Language and Information Technologies', null),
('MS', 'Literature, Media, and Communication', 'LMC'),
('MS', 'Management', 'MGT'),
('MS', 'Materials Science and Engineering', 'MSE'),
('MS', 'Mathematics', 'MATH'),
('MS', 'Mechanical Engineering', 'ME'),
('MS', 'Medical Physics', 'MP'),
('MS', 'Music Technology', null),
('MS', 'Nuclear Engineering', null),
('MS', 'Operations Research', null),
('MS', 'Physics', 'PHYS'),
('MS', 'Psychology', 'PSYC'),
('MS', 'Public Policy', 'PUBP'),
('MS', 'Quantitative and Computational Finance', null),
('MS', 'Robotics', null),
('MS', 'Statistics', null),
('MS', 'Supply Chain Engineering', null),
('MS', 'Sustainable Energy', null),
('MS', 'Urban Design', null),
('MS', 'Urban Analytics', null),

-- init all the PhD Majors
('Phd', 'Aerospace Engineering', 'AE'),
('Phd', 'Algorithms, Combinatorics, and Optimization', null),
('Phd', 'Applied Physiology', null),
('Phd', 'Architecture', 'ARCH'),
('Phd', 'Bioengineering', null),
('Phd', 'Bioinformatics', null),
('Phd', 'Biology', 'BIOL'),
('Phd', 'Biomedical Engineering', 'BMED'),
('Phd', 'Building Construction', 'BC'),
('Phd', 'Chemical Engineering', null),
('Phd', 'Chemistry', 'CHEM'),
('Phd', 'City and Regional Planning', null),
('Phd', 'Civil Engineering', 'CEE'),
('Phd', 'Computational Science and Engineering', 'CSE'),
('Phd', 'Computer Science', 'CS'),
('Phd', 'Digital Media', null),
('PhD', 'Earth and Atmospheric Sciences', 'EAS'),
('PhD', 'Economics', 'ECON'),
('Phd', 'Electrical and Computer Engineering', 'ECE'),
('Phd', 'Engineering Science and Mechanics', null),
('Phd', 'Enviromental Engineering', null),
('Phd', 'History and Sociology of Technology and Science', null),
('Phd', 'Human-Centered Computing', null),
('Phd', 'Industrial Engineering', 'ISYE'),
('Phd', 'International Affaris, Science, and Technology', null),
('Phd', 'Machine Learning', null),
('Phd', 'Management', 'MGT'),
('Phd', 'Materials Science and Engineering', 'MSE'),
('Phd', 'Mathematics', 'MATH'),
('Phd', 'Mechanical Engineering', null),
('Phd', 'Music Technology', null),
('Phd', 'Nuclear Engineering', null),
('Phd', 'Ocean Science and Engineering', null),
('Phd', 'Operations Research', null),
('Phd', 'Physics', 'PHYS'),
('Phd', 'Psychology', 'PYSC'),
('Phd', 'Public Policy', 'PUBP'),
('Phd', 'Quantitative Biosciences', null),
('Phd', 'Robotics', null)
;







/* Might init these values from the OSCAR Crawler directly
INSERT INTO subject (subject_code) 
VALUES 
('ACCT'), ('AE'), ('AAPH'), ('ARCH'), ('BS'), ('BIO'), ('BMED'), ('CEE'), ('CETL'), ('CHBE'), ('CHEM'),
('CHIN'), ('COA'), ('COE'), ('CS'), ('DAT'), ('EAS'), ('ECE'), ('ECON'), ('ENGL'), ('FREN'), ('GRMN'),
('GT'), ('HIST'), ('ID'), ('INTA'), ('ISYE'), ('KOR'), ('LING'), ('LMC'), ('MATH'), ('MCAT'), ('ME'),
('MGT'), ('MSE'), ('MUSI'), ('NRE'), ('PHIL'), ('PHYS'), ('POL'), ('PSYC'), ('PTFE'), ('PUBP'), ('SOC'),
('SAPN');
*/