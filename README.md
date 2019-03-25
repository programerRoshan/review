# reviewForm
This a simple webservice to give feedback from students to faculty

## installtion and run process

# creation of virtualenv
python -m virtualenv venv

# activate virtualenv
venv\Scripts\activate

# install packages
pip install -r requirements.txt

# initial process
python manage.py makemigrations

python manage.py migrate

python manage.py collectstatic

# create superuser to access admin
python manage.py createsuperuser

python manage.py runserver

## add group(s) for usage
# usage: python manage.py addGroup <GROUP_NAME>

python manage.py addGroup Faculty

python manage.py addGroup Student #optional

# add users to groups

python manage.py setGroup <GROUP_NAME> <USER_NAME_LIST>

# currently using "django.core.mail.backends.console.EmailBackend"

# add password for "django.core.mail.backends.smtp.EmailBackend"
