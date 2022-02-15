 # Predict Missing Words 

A web project to fill up sentences with correct words.  

# Setup

To install the project, run the following commands:  
```
# create and activate a virtual environment
$ pip install -r requirements.txt
$ python manage.py runserver

And then go to http://localhost:8000/.  
```

# Load data

Load generated data from the algorithm to the django database using loaddata.p module, which is located in the project root.  

# Superuser
```
python3 manage.py createsuperuser
```
And you can go to http://localhost:8000/admin/ to login.

# login
http://localhost:8000/accounts/login/

# register
http://localhost:8000/accounts/register/
