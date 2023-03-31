# Database Priming

These Python scripts are used to prime the database with course and/or static data. 

The database tables are populated in the following order:
- `subject`
- `major`
- `semester`
- `instructor`
- `class`
- `location`

> **Warning** All entries in the corresponding tables are deleted before the new entries are inserted.  

### Dependencies

*   tqdm
*   sqlalchemy

<br>
<br>

## Course Data Primer (`course_data_primer.py`)

The database can be primed with course data from either a file or by scraping it directly from OSCAR.

Tables primed:
- `semester`
- `instructor`
- `class`
- `location`

Source of data;
- OSCAR, or .pkl file

### How to Run

To prime the database directly from OSCAR run the script using the command line by passing the following arguments:

```python
python course_data_extractor.py --oscar <semester> <year>
```
where `<semester>` is the name of the semester [`spring`|`summer`|`fall`], `<year>` is the year. Example:
```python
python course_data_extractor.py --semester fall 2023
```

<br>

Alternatively, you can prime the database from a .pkl file previously obtained from `course_scraper.py` by passing the following arguments:

```python
python course_data_extractor.py --file <filepath>
```
where`<filepath>` is the path to the file containing the course data. Example:

```python
python course_data_extractor.py --file fall_2023_1680156704.pkl
```

Only one of `--semester` and `--file` can be used at a time.

<br>
<br>

## Static Data Primer (`static_data_primer.py`)

Tables primed:
- `major`
- `subject`

Source of data;
- `major`: `static_data/majors.py`
- `subject`: `static_data/subject_codes.py`

### How to Run


```python
python static_data_primer.py
```
