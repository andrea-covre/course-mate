use course_mate;

INSERT INTO subject(code, name) 
VALUES 
('AE', 'Aerospace Engineering'),
('ARCH', 'Architecture'),
('BIOL', 'Biology'),
('BMED', 'Biomedical Engineering'),
('BC', 'Building Construction'),
('CHBE', 'Chemical and Biomolecular Engineering'),
('CHEM', 'Chemistry'),
('CEE', 'Civil Engineering'),
('ECE', 'Computer Engineering'),
('CS', 'Computer Science'),
('EAS', 'Earth and Atmospheric Sciences'),
('ECON', 'Economics'),
('EE', 'Electrical Engineering'),
('HTS', 'History, Technology, and Society'),
('ID', 'Industrial Design'),
('ISYE', 'Industrial Engineering'),
('INTA', 'International Affairs'),
('LMC', 'Literature, Media, and Communication'),
('MSE', 'Materials Science and Engineering'),
('MATH', 'Mathematics'),
('ME', 'Mechanical Engineering'),
('NEUR', 'Neuroscience'),
('NRE', 'Nuclear and Radiological Engineering'),
('PHYS', 'Physics'),
('PYSC', 'Psychology'),
('PUBP', 'Public Policy'),
('CSE', 'Computational Science and Engineering'),
('GMC', 'Global Media and Cultures'),
('HCI', 'Human-Computer Interaction'),
('IL', 'International Logistics'),
('MP', 'Medical Physics'),
('MGT', 'Management'),
('HS', 'Health Systems');

INSERT INTO major (level, name) 
VALUES 
-- init all the UG Majors
('BS', 'Aerospace Engineering'),
('BS', 'Applied Languages and Intercultural Studies'),
('BS', 'Architecture'),
('BS', 'Applied Physics'),
('BS', 'Biochemistry'),
('BS', 'Biology'),
('BS', 'Biomedical Engineering'),
('BS', 'Building Construction'),
('BS', 'Business Administration'),
('BS', 'Chemical and Biomolecular Engineering'),
('BS', 'Chemistry'),
('BS', 'Civil Engineering'),
('BS', 'Computational Media'),
('BS', 'Computer Engineering'),
('BS', 'Computer Science'),
('BS', 'Earth and Atmospheric Sciences'),
('BS', 'Economics'),
('BS', 'Economics and International Affairs'),
('BS', 'Electrical Engineering'),
('BS', 'Environmental Engineering'),
('BS', 'Global Economics and Modern Languages'),
('BS', 'History, Technology, and Society'),
('BS', 'Industrial Design'),
('BS', 'Industrial Engineering'),
('BS', 'International Affairs'),
('BS', 'International Affairs and Modern Languages'),
('BS', 'Literature, Media, and Communication'),
('BS', 'Materials Science and Engineering'),
('BS', 'Mathematics'),
('BS', 'Mechanical Engineering'),
('BS', 'Music Technology'),
('BS', 'Neuroscience'),
('BS', 'Nuclear and Radiological Engineering'),
('BS', 'Physics'),
('BS', 'Psychology'),
('BS', 'Public Policy'),

-- init all the GRAD Majors
('MS', 'Aerospace Engineering'),
('MS', 'Analytics'),
('MS', 'Applied Languages and Intercultural Studies'),
('MS', 'Architecture'),
('MS', 'Bioengineering'),
('MS', 'Bioinformatics'),
('MS', 'Biology'),
('MS', 'Biomedical Engineering'),
('MS', 'Building Construction and Facility Managment'),
('MS', 'Business Administration (MBA)'),
('MS', 'Chemical and Biomolecular Engineering'),
('MS', 'Chemical Engineering'),
('MS', 'Chemistry'),
('MS', 'Civil Engineering'),
('MS', 'City and Regional Planning & Civil Engineering'),
('MS', 'Computational Media & Digital Media'),
('MS', 'Computational Science and Engineering'),
('MS', 'Computer Science'),
('MS', 'Cybersecurity'),
('MS', 'Digital Media'),
('MS', 'Earth and Atmospheric Sciences'),
('MS', 'Economics'),
('MS', 'Electrical Engineering'),
('MS', 'Electrical and Computer Engineering'),
('MS', 'Engineering Science and Mechanics'),
('MS', 'Environmental Engineering'),
('MS', 'Geographic Information Science and Technology'),
('MS', 'Global Development'),
('MS', 'Global Media and Cultures'),
('MS', 'Health Systems'),
('MS', 'History and Sociology of Technology and Science'),
('MS', 'Human-Computer Interaction'),
('MS', 'Industrial Design'),
('MS', 'Industrial Engineering'),
('MS', 'International Affairs'),
('MS', 'International Logistics'),
('MS', 'Language and Information Technologies'),
('MS', 'Literature, Media, and Communication'),
('MS', 'Management'),
('MS', 'Materials Science and Engineering'),
('MS', 'Mathematics'),
('MS', 'Mechanical Engineering'),
('MS', 'Medical Physics'),
('MS', 'Music Technology'),
('MS', 'Nuclear Engineering'),
('MS', 'Operations Research'),
('MS', 'Physics'),
('MS', 'Psychology'),
('MS', 'Public Policy'),
('MS', 'Quantitative and Computational Finance'),
('MS', 'Robotics'),
('MS', 'Statistics'),
('MS', 'Supply Chain Engineering'),
('MS', 'Sustainable Energy'),
('MS', 'Urban Design'),
('MS', 'Urban Analytics'),

-- init all the PhD Majors
('Phd', 'Aerospace Engineering'),
('Phd', 'Algorithms, Combinatorics, and Optimization'),
('Phd', 'Applied Physiology'),
('Phd', 'Architecture'),
('Phd', 'Bioengineering'),
('Phd', 'Bioinformatics'),
('Phd', 'Biology'),
('Phd', 'Biomedical Engineering'),
('Phd', 'Building Construction'),
('Phd', 'Chemical Engineering'),
('Phd', 'Chemistry'),
('Phd', 'City and Regional Planning'),
('Phd', 'Civil Engineering'),
('Phd', 'Computational Science and Engineering'),
('Phd', 'Computer Science'),
('Phd', 'Digital Media'),
('PhD', 'Earth and Atmospheric Sciences'),
('PhD', 'Economics'),
('Phd', 'Electrical and Computer Engineering'),
('Phd', 'Engineering Science and Mechanics'),
('Phd', 'Enviromental Engineering'),
('Phd', 'History and Sociology of Technology and Science'),
('Phd', 'Human-Centered Computing'),
('Phd', 'Industrial Engineering'),
('Phd', 'International Affaris, Science, and Technology'),
('Phd', 'Machine Learning'),
('Phd', 'Management'),
('Phd', 'Materials Science and Engineering'),
('Phd', 'Mathematics'),
('Phd', 'Mechanical Engineering'),
('Phd', 'Music Technology'),
('Phd', 'Nuclear Engineering'),
('Phd', 'Ocean Science and Engineering'),
('Phd', 'Operations Research'),
('Phd', 'Physics'),
('Phd', 'Psychology'),
('Phd', 'Public Policy'),
('Phd', 'Quantitative Biosciences'),
('Phd', 'Robotics')
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