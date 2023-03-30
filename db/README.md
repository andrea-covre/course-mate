## Course Data Primer (`course_data_primer.py`)

This Python script is used to extract course data and prime it into a database. The database can be primed from either a file or by scraping course data directly from OSCAR.

The database tables are populated in the following order:
- `semester`
- `instructor`
- `class`
- `location`

> **Warning** All entries in the corresponding tables are deleted before the new entries are inserted.  

### Dependencies

*   tqdm
*   sqlalchemy

### How to Run

To prime the database directly from OSCAR run the script using the command line by passing the following arguments:

```python
python course_data_extractor.py --semester <semester> <year>
```
where `<semester>` is the name of the semester [`spring`|`summer`|`fall`], `<year>` is the year. Example:
```python
python course_data_extractor.py --semester fall 2023
```
<br>
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