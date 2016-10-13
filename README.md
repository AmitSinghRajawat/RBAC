# RBAC
Role based access control

Description:
In our web-service we have three layers.
1. Application Layer
2. Database
3. Models

APIs used are:
1. assign_roles:
endpoint: /users/{user_id}/role/{role_id}
type: POST
2. remove_roles:
endpoint: /users/{user_id}/role/{role_id}
type: DELETE
3. check_authorization:
endpoint: /users/{user_id}/resource/{resource_id}/access_type/{access_id}
type: GET

Assumptions:
1. We have following services.
	Gunicorn container to host web-service in django
	Logging system to capture debug and error logs for each reuqest
2. Dummy users to perform actions upon, initially they don't have any permissions.
3. Dummy resources created in DB.
4. Dummy roles, based on roles given assuming some permissions.
5. Permission '110' corresponds to RWD (Read, Write, Delete).
	i.e. Read yes, Write yes, Delete no

Workflow:
1. Client interacts with the application layer via RESTful service.
2. Application layers talks to client, based on API calls.
3. API interacts with database layer and model layer.

How to launch the application:
1. Install python IDE atleast 2.7
2. Go to the path where application.py file is present.
3. run the command from CLI.
	python application.py
