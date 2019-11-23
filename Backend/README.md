# COMP354Project
COMP 354 Project 
Instructions:
1. Install [Python 3.6.0](https://www.python.org/downloads/release/python-360/)
   * Make sure its added to your PATH variable.
   * run from command line/terminal `python -V` to ensure your python version is 3.6.0
2. Install WAMP/LAMP
   * (For Windows) Install [WAMP](https://sourceforge.net/projects/wampserver/)
   * (For Mac) Follow thses [Installation Instructions](https://jasonmccreary.me/articles/install-apache-php-mysql-mac-os-x/)
   * (for Debian based Linux): [Installation Instructions](https://howtoubuntu.org/how-to-install-lamp-on-ubuntu)
3. Clone this repository make sure you are located in the **Backend/** Directory
4. In your terminal/console Run:
5. `pip install virtualenv`
6. `cd thestars/`
7.  `source bin/activate` (or) `source Scripts/activate.bat`
8. `pip install -r requirements.txt`
9. run 'python manage.py createsuperuser', then enter 'admin', passcode 'thestarsadmin'(to be consistency in all tests)
10. Edit settings.py USER and PASSWORD under DATABASES, put your MySQL username and password, there. 
11. Login to MySQL Terminal or MySQL Manager
12. run `create database thestars` on terminal or create database using MySQL Manager
13. run `python manage.py makemigrations`
14. run `python manage.py migrate`
15. run `python manage.py runserver localhost:443` or `python manage.py runserver 127.0.0.1:443`

You are able to visit the backend system 127.0.0.1:443 now.
path: 127.0.0.1:443/xadmin   to access backend dashboard
path: 127.0.0.1:443/docs   to access project docs

Remote server address: http://173.249.5.177:443/
nohup python3 manage.py runserver 0.0.0.0:443 &

Make MySQL Data Structure in pycharm:
Tools -> Run manage.py Task -> makemigrations (Populate the data changes)
Tools -> Run manage.py Task -> migrate (Populate the data structure in MySQL)

========================================================================================================================================

System requirement

pip install .....
System Requirement:
* Python 3.6
* Django 1.11.6 !!!!
* djangoframework        ?
* markdown (for browsable API)
* django-filter
* pillow (for picture handling)
* DjangoUeditor (provided in extra_app folder)
* coreapi   (for documentation)
* django-guardian  (object level permission)
* django-cors-headers
* * djangoframework-jwt      ?

xadmin required dependencies:
* django-crispy-form
* django-reversion
* django-formtools
* future
* httplib2
* six
* xlwt 
* xlsxwriter

Make MySQL Data Structure:
Tools -> Run manage.py Task -> makemigrations (Populate the data changes)
Tools -> Run manage.py Task -> migrate (Populate the data structure in MySQL)
OR: python manage.py .... in Console

1: Once the model structure changes, first use makemigrations to populate the py script and
use command migrate to execute the changes in MySQL
2: Before system online, make sure to create a superuser by command: createsuperuser
(admin: thestars)


Changes:
1: Under GoodsCategoryBrand model, the path of image should be "brands/" instead of "brands/images"

* Frontend calls should call "127.0.0.1:8000/api-token-auth/" with username and 
password in JSON in http header to get auth token.

* For front end. When using the API which requires auth, use Scheme 'JWT'



