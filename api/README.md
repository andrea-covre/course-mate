# APIs

## List of APIs implemented
### User

| Request Method | Endpoint | Description |
| --- | --- | --- |
| `GET` | `/users?id=<user\_id>` | Gets user given the user id |
| `POST` | `/users/add` | Creates new user |
| `DELETE` | `/users/delete?id=<user\_id` | Deletes user given the user id |

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