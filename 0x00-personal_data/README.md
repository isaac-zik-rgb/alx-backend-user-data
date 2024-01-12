# 0x00-personal_data
# Requirements
## General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/env python3
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle style (version 2.5)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
* All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
* Your code should not be executed when imported (by using if __name__ == "__main__":)
## Tasks
### 0. Regex-ing
Write a function called filter_datum that returns the log message obfuscated:
* Arguments: fields, a list of strings representing all fields to obfuscate
* A string representing a log message
* The function should use a regex to replace occurrences of certain field values
* Credit card numbers must have their number replaced with **** **** **** <last 4 digits>
* Email addresses must have their user name replaced with **** and the domain name replaced with ****
* Passwords must have their value replaced with ****
```
