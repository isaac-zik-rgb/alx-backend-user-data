# 0x02-Session_authentication
# Specializations - Web Stack programming ― Back-end    
# By Guillaume, CTO at Holberton School
# Ongoing project - started 09-13-2021, must end by 09-17-2021 (in 1 day) - you're done with 0% of tasks.
## Background Context
In this project, you will implement a Session Authentication.
The authentication system is a very important concept for web applications. It is
the mechanism whereby users can prove their identity. It is essential that the
user can only access their own resources and not those of other users. It is
also the basis for implementing access control.
## Resources
### Read or watch:
- [REST API Authentication Mechanisms](https://www.youtube.com/watch?v=501dpx2IjGY)
- [Base64 in Python](https://docs.python.org/3.7/library/base64.html)
- [HTTP header Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Authorization)
- [Flask](https://palletsprojects.com/p/flask/)
- [Flask Cookie Jar](https://werkzeug.palletsprojects.com/en/0.15.x/wrappers/#werkzeug.wrappers.BaseRequest.cookies)
## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone,
without the help of Google:
### General
- What authentication means
- What session authentication means
- What Cookies are
- How to send Cookies
- How to parse Cookies
## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3
(version 3.7)
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- You are not allowed to use the Flask-HTTPAuth module
- You are not allowed to use the Flask-WTF module
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
## Setup
### Install Flask
$ pip3 install Flask
### Install flasgger