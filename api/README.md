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

```bash
python -m api.api
```

### Run the unittests
Make sure the API server is running before running the tests.
```bash
python -m api.tests.runner
```