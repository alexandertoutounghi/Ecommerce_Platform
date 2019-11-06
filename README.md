# COMP354Project
COMP 354 Project 
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

* SERVER SETUP
https://www.lizenghai.com/archives/23484.html
nohup python3 manage.py runserver 0.0.0.0:443 &


-----> http://173.249.5.177:443/

* start env:
cd thestars/
source bin/activate
deactivate
python -V


