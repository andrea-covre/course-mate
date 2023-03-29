# Course Scraper Documentation

This code allows users to extract course information from the Georgia Tech OSCAR system. The information that can be extracted includes the course name, section ID, CRN, and other details.

### Import Statements

The following import statements are used:

*   pickle - used for serializing and deserializing Python objects.
*   argparse - used for parsing command-line arguments.
*   requests - used for sending HTTP requests to a website.
*   time - used for generating a unique filename.
*   BeautifulSoup - used for parsing HTML.

Additionally, the `data_extractor` module is imported, which defines a function that extracts course data from an HTML document.

### Constants

*   `URL` - the URL of the OSCAR search page that is used to extract course data.
*   `HEADERS` - a dictionary containing various header values used in the HTTP requests.
*   `BASE_DATA` - a list of tuples containing the initial data to be sent in the HTTP request.
*   `SUBJECTS_LIST` - a list of all subject codes that are used to search for courses.
*   `SEMESTER_TO_MONTH` - a dictionary that maps semester names to their corresponding month values (in integers).

### Functions

#### `parse_args()`

This function uses the `argparse` module to parse the command-line arguments. It accepts two arguments, `semester` and `year`, and returns the parsed arguments.

#### `get_request_data_body(year, semester)`

This function creates the data that is sent in the HTTP request. It takes the `year` and `semester` as input and returns a list of tuples containing the data.

#### `main()`

This is the main function of the program. It first parses the command-line arguments using `parse_args()`. It then uses the `get_request_data_body()` function to generate the data to be sent in the HTTP request. It sends the HTTP request to the OSCAR search page, and if successful, extracts the course data using the `extract_data()` function defined in the `data_extractor` module. Finally, it saves the extracted data to a file with a unique name.

### Example usage

To extract course information for the Fall 2023 semester, run the following command:

python

```python
python oscar_scraper.py fall 2023
```

This will generate a file with the format `fall_2023_<timestamp>.pkl` in the current directory, where `<timestamp>` is a Unix timestamp indicating the time the file was generated. The file will contain a list of dictionaries, where each dictionary represents a course section and contains information such as the course name, section ID, and CRN.