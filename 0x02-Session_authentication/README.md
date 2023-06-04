# 0x02. Session authentication


> This repository contains the tasks for `Session authentication` project and a description of what each program or function does:


## Learning Objectives

	* What authentication means
	* What session authentication means
	* What Cookies are
	* How to send Cookies
	* How to parse Cookies


* Authentication is the process of verifying the identity of a user or entity attempting to access a system or application. It ensures that the user is who they claim to be before granting access to sensitive information or performing certain actions. In Python, there are several ways to implement authentication:

1. Username and Password Authentication:
* This method involves validating a user's identity using a username and password combination.

2. Token-based Authentication:
* Token-based authentication involves issuing a token (such as JSON Web Tokens or JWTs) to a user after successful login, which is then used to authenticate subsequent requests. 


---

# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
