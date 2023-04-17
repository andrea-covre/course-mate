# APIs

## List of APIs implemented
### User

| Request Method | Endpoint | Description | Body | Has Unittest |
| --- | --- | --- | --- | --- |
| `GET` | `/users?id=<user_id>` | Gets user given the user id | | Yes |
| `POST` | `/users/add` | Creates new user | {<br>"email_address": <br> "edu_email_address": <br> "first_name": <br> "last_name": <br> "phone_number": <br> "grad_year": <br> "major_id": <br> }| Yes |
| `DELETE` | `/users/delete?id=<user_id>` | Deletes user given the user id | | Yes |

### Schedule

| Request Method | Endpoint | Description | Body | Has Unittest |
| --- | --- | --- | --- | --- |
| `POST` | `/schedule/add` | Adds a section to the user schedule | {<br>"user_id": <br> "semester_id": <br> "crn": <br> } <br> *or* --- <br> {<br>"user_id": <br> "semester_id": <br> "subject_code": <br> "class_number": <br> "section_code": <br> } | Yes |
| `GET` | `/schedule/?id=<user_id>&semester=<semester_id>` | Gets a user schedule given its id and semester id. Returns a list of tuples of the form `(class_title, cladd_subject, class_number, section_code, crn, section_id)`|  | No |
| `GET` | `/schedule/common?id_1=<user_id_1>&id_2=<user_id_2>&semester=<semester_id>` | Gets the common classes given two users ids and semester id. Returns a list of tuples of the form `(class_title, cladd_subject, class_number, section_code, crn, section_id)`|  | No |

### Major
| Request Method | Endpoint | Description | Has Unittest |
| --- | --- | --- | --- |
| `GET` | `/majors` | Gets all majors and their corresponding id | Yes |

## Instructions

### Run the API Server

#### Run the API Server Locally
To run the server locally on port `5000`, run the following command:
```bash
python -m api.api
```

#### Run the API Server Publicly
To run the server publicly on port `8080`, run the following command:
```bash
python -m api.api -p
```

---

### Run the unittests
Make sure the API server is running before running the tests.

#### Run the unittests Locally
```bash
python -m api.tests.runner
```

#### Run the unittests on Public Address
```bash
python -m api.tests.runner [-p <public_address>]
```