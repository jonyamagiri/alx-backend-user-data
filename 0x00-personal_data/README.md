# 0x00. Personal data

> This repository contains the tasks for `Personal data` project and a description of what each program or function does:


## Learning Objectives

	* Examples of Personally Identifiable Information (PII)
	* How to implement a log filter that will obfuscate PII fields
	* How to encrypt a password and check the validity of an input password
	* How to authenticate to a database using environment variables


* Personally Identifiable Information (PII) refers to any information that can be used to identify an individual. In the context of Python, PII can include various types of data such as names, addresses, social security numbers, email addresses, phone numbers, and more. It is important to handle PII with care to protect individuals' privacy and comply with data protection regulations.


## Tasks

- [x] Task: filtered_logger.py
0. Regex-ing
* Write a function called `filter_datum` that returns the log message obfuscated:
1. Log formatter
* Implement the `format` method to filter values in incoming log records using `filter_datum`. Values for fields in `fields` should be filtered.
2. Create logger
* Implement a `get_logger` function that takes no arguments and returns a `logging.Logger` object.
3. Connect to secure database
* Implement a `get_db` function that returns a connector to the database (`mysql.connector.connection.MySQLConnection` object).
4. Read and filter data
* Implement a `main` function that takes no arguments and returns nothing.

- [x] Task: encrypt_password.py
5. Encrypting passwords
Implement a `hash_password` function that expects one string argument name `password` and returns a salted, hashed password, which is a byte string.
6. Check valid password
Implement an `is_valid` function that expects 2 arguments and returns a boolean.


___


