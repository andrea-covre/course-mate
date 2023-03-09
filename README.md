# course-mate

For internal use only: to connect to database and use API, add a password field to the SQLConnectionObject in connection.py. 

Example:

self.password = $your_password$

Localhost API Documentation:

http://127.0.0.1:5000/users?id=<user_id> -> Retrieve account data for provided user ID (GET)

http://127.0.0.1:5000/users/add -> Create account for user by passing atleast all mandatory fields as per schema. (POST)

http://127.0.0.1:5000/users/update/email -> Update user email for provided user ID (PUT)

http://127.0.0.1:5000/users/update/edu_email -> Update user .edu email for provided user ID (PUT)

http://127.0.0.1:5000/users/update/first_name -> Update user first name for provided user ID (PUT)

http://127.0.0.1:5000/users/update/last_name -> Update user last name for provided user ID (PUT)

http://127.0.0.1:5000/users/update/phone_number -> Update user phone number for provided user ID (PUT)

http://127.0.0.1:5000/users/update/major_id -> Update user major ID for provided user ID (PUT)

http://127.0.0.1:5000/users/update/grad_year -> Update user graduation year for provided user ID (PUT)
