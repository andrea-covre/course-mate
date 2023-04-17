# APIs

## List of APIs implemented
### User

| Request Method | Endpoint | Description | Body |
| --- | --- | --- | --- |
| `GET` | `/users?id=<user_id>` | Gets user given the user id | |
| `POST` | `/users/add` | Creates new user | {<br>"email_address": <br> "edu_email_address": <br> "first_name": <br> "last_name": <br> "phone_number": <br> "grad_year": <br> "major_id": <br> }|
| `DELETE` | `/users/delete?id=<user_id>` | Deletes user given the user id | |

### Major
| Request Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/majors` | Gets all majors and their corresponding id |

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
python -m api.api
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