# Quiz


##Installations

Clone/ Download this repository.

Installing dependencies
It will install all required dependies in the project.
pip install -r requirements.txt

Migrations
To run migrations.
python manage.py makemigrations
python manage.py migrate

Create superuser
To create super user run.
python manage.py createsuperuser
After running this command it will ask for username, password. You can access admin panel from localhost:8000/admin/

Running locally
To run at localhost. It will run on port 8000 by default.
python manage.py runserver

# Instructions 

1) ### Installations
  Make sure to have python version 3 install on you pc or laptop. 
  If not install it from [here](https://www.python.org) <br>
  **Clone repository** <br>
  `https://github.com/sswapnil2/django-quiz-app.git`<br>
  `cd django-quiz-app`
  
2) ### Installing dependencies 
  It will install all required dependies in the project.<br>
  `pip install -r requirements.txt`
  
3) ### Migrations 
  To run migrations. <br>
  `python manage.py makemigrations`<br>
  `python manage.py migrate`
  
4) ### Create superuser
  To create super user run. <br>
  `python manage.py createsuperuser` <br>
  After running this command it will ask for username, password.
  You can access admin panel from `localhost:8000/admin/`

4) ### Running locally
  To run at localhost. It will run on port 8000 by default.<br>
  `python manage.py runserver` 
