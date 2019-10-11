# COMP354Project
COMP 354 Project 
System requirement

pip install .....
System Requirement:
* Python 3.6
* Django 1.11.3 !!!!
* djangoframework
* markdown (for browsable API)
* django-filter
* pillow (for picture handling)
* DjangoUeditor (provided in extra_app folder)

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
