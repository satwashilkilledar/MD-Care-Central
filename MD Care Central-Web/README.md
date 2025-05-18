# MDTouch
Mdtouch website to control database and manage the framework request.
ML in disease search and prediction based on symptoms.

-- To make this repo work:
 - Install requirements.txt in a virtual enviornment
 To craete a virtualenv,
 	pip install virtualenv
 	or
 	pip3 install virtualenv 
 To create a virtual env:
 	virtualenv venv 
 - Activate venv
 	> source venv/bin/activate
 - Using fish shell:
 	> source venv/bin/activate.fish
 - To deactivate:
 	> deactivate

## install dependencies-
goto project root directory and use the command -
	> pip install -r requirements.txt
- or
	> pip3 install -r requirements.txt

## Run project-
from the root directory use commands:

	> To consider changes in DB : python manage.py makemigrations

	> To commit changes in DB : python manage.py migrate

	> To run server - python manage.py runserver

## To create administrator account in mdtouchs website:- 
use command:- 

	> python manage.py createsuperuser

Then enter the username, email and password.

Now you can log in to it from the < websitelink >/admin. Eg: http://127.0.0.1:8000/admin

## To see the complete project working-
you are required to enter some data in DB from the website admin page,
eg: create hospital, create doctors, create patient, create admin, create blook banks, etc

## while using software:
The weburls are hardcoded, so you have to chnage the web url link according to the hosted URL on the server and corresponding change the folder names so as to get a nice representation of icons.

# Enjoy this amazing administration ^_^!!