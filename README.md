Follow these instruction to run the project in cmd

Step  1=> Download latest version Python
Step  2=> check python version `python --version`
Step  3=> check pip version `pip --version`
Step  4=> install virtual environment  `pip install virtualenv`
Step  5=> after installation we need to create virtualenv
Step  6=> create venv `virtualenv -p python venv` (venv - environment name)
Step  7=> cd communitypath From venv
Step  8=> now activate the venv `venv\Scripts\activate` after creation you got this view (venv) D://Folder..
Step  9=> finally, this project want to be few pakages.
Step 10=> `cd sector_project` - identifing the folder before manage.py, secotorapp folder and more files
Step 11=> last step `pip install -r requirements.txt`
Step 12=> run XAMPP server apache and mysql
Step 13=> create database name `sector_local`
Step 14=> now add a table in database so we write in cmd `python manage.py makemigrations`
Step 15=> without error, add a tables `python manage.py migrate` now check the tables all are here in DB!
Step 16=> All are statisfied. write in cmd `python manage.py runserver`
You got like this url use ctrl+click see the UI 
http://127.0.0.1:8000/

create new user click `signup`
