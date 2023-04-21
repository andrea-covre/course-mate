# APIs

## Authentication
Requests must be sent with the following header:
`{'Authorization': API_TOKEN}`

## List of APIs implemented
### User

| Request Method | Endpoint | Description | Body | Has Unittest |
| --- | --- | --- | --- | --- |
| `GET` | `/users?id=<user_id>` | Gets user given the user id (can also get user by: `phone_number` \| `email` \| `edu_email` \| (`first_name & last_name`) | | Yes |
| `POST` | `/users/add` | Creates new user | {<br> "id": <br> "email_address": <br> "edu_email_address": <br> "first_name": <br> "last_name": <br> "phone_number": <br> "grad_year": <br> "major_id": <br> }| Yes |
| `DELETE` | `/users/delete?id=<user_id>` | Deletes user given the user id | | Yes |

### Schedule

| Request Method | Endpoint | Description | Body | Has Unittest |
| --- | --- | --- | --- | --- |
| `POST` | `/schedule/add` | Adds a section to the user schedule | {<br>"user_id": <br> "semester_id": <br> "crn": <br> } <br> *or* --- <br> {<br>"user_id": <br> "semester_id": <br> "subject_code": <br> "class_number": <br> "section_code": <br> } | Yes |
| `GET` | `/schedule/?id=<user_id>&semester=<semester_id>` | Gets a user schedule given its id and semester id. Returns a list of dictionaries with `title`, `class_subject`, `class_number`, `section_code`, `crn`, `section_id` as keys |  | No |
| `GET` | `/schedule/common?id_1=<user_id_1>&id_2=<user_id_2>&semester=<semester_id>` | Gets the common classes given two users ids and semester id. Returns a list of dictionaries with `class_title`, `class_subject`, `class_number`, `section_code`, `crn`, `section_id` as keys |  | No |

### Major
| Request Method | Endpoint | Description | Has Unittest |
| --- | --- | --- | --- |
| `GET` | `/majors` | Gets all majors and their corresponding id | Yes |

### Friendship
| Request Method | Endpoint | Description | Has Unittest |
| --- | --- | --- | --- |
| `GET` | `/friendship/request?sender_id=<sender_id>&receiver_id=<receiver_id>` | Create a friendship request from sender_id to receiver_id | No |
| `GET` | `/friendship/accept?sender_id=<sender_id>&receiver_id=<receiver_id>` | Accept a friendship request from sender_id to receiver_id | No |
| `GET` | `/friendship/delete?user1_id=<sender_id>&user2_id=<receiver_id>` | Delete a friendship request from user1_id to user2_id | No |
| `GET` | `/friendship/list?user_id=<user_id>` | Get all friendships given the user_id, returns a dictionary of the form: `{"friends": [list of ids], "incoming_requests": [list of ids], "outgoing_requests": [list of ids]}` | No |
| `GET` | `/friendship/get_by_section?user_id=<user_id>&section_id=<section_id>` | Get all friends taking a given section, returns a list of dictionaries with `first_name`, `last_name`, `id` as keys. | No |

### Semester
| Request Method | Endpoint | Description | Has Unittest |
| --- | --- | --- | --- |
| `GET` | `/semester` | Get all semesters, returns a list of dictionaries with `id`, `term`, `year` as keys | No |

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