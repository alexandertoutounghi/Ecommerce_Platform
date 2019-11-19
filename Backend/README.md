# COMP354Project
COMP 354 Project 
Instruction:

Pre-setup
* 1: use 'python -V' to ensure your python version is 3.6.x
* 2: install virtue environment
 google "install python virture environment" to find your system specific commands

Setup:
* 1: Assuming you already setup the virtue environment, if not, please search it online.
* 2: Once you setup the virtue environment, two folders named bin and lib are supposed be there. Not there? The
    virtue environment is not setup properly. 
* 3: Create a database named 'thestars' in you Mysql system.
* 4: Change the mysql connection parameters in setting.py DATABASES = {.....} with your db credential
* 5: run 'pip install -r requirements.txt' to install all dependencies.
* 6: run 'python manage.py createsuperuser', then enter 'admin', passcode 'thestarsadmin'(to be consistency in all tests)
* 7: In console, cd to you project folder, run command python manage.py makemigrations (populate the py db script)
* 8: In console, run command python manage.py migrate (Populate the data structure in MySQL)
* 9: run 'python manage.py runserver 127.0.0.1:443'.

You are able to visit the backend system 127.0.0.1:443 now.
path: 127.0.0.1:443/xadmin   to access backend dashboard
path: 127.0.0.1:443/docs   to access project docs


Remote server address: http://173.249.5.177:443/
nohup python3 manage.py runserver 0.0.0.0:443 &




Make MySQL Data Structure in pycharm:
Tools -> Run manage.py Task -> makemigrations (Populate the data changes)
Tools -> Run manage.py Task -> migrate (Populate the data structure in MySQL)




* For front end. When using the API which requires auth, use Scheme 'JWT'

* SERVER SETUP
https://www.lizenghai.com/archives/23484.html
nohup python3 manage.py runserver 0.0.0.0:443 &

* start env:
cd thestars/
source bin/activate
deactivate
python -V


