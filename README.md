# logs4free
Display logs from web server log files (apache, nginx) in your brouser in real time mode.

# INSTALL

## Install python and django
[django](https://docs.djangoproject.com/en/1.8/intro/install/)

## Install python mysqldb connector
[mysqldb connector](http://mysql-python.sourceforge.net/MySQLdb.html#installation)

## Install mysql
[mysql server, client](http://dev.mysql.com/doc/refman/5.7/en/installing.html)

## Create database for logs storing
'''
CREATE DATABASE `log4free` CHARACTER SET utf8 COLLATE utf8_general_ci;
'''


# SETTINGS

## Export django-settings-module to environments variables

From your logs4free directory:
'''
export DJANGO_SETTINGS_MODULE=log4free.settings
'''

## Database password
Specify database password in logs4free/log4free.settings.py file. You can find the customize marker there.


# USAGE

## Start the logs storing

From your logs4free directory:
'''
python tailer.py /var/log/apache2/access.log &
'''

This will run the logs storage process in background mode. You can use other path for logs location.

## Start the web app
From your logs4free directory:
'''
python manage.py runserver 0.0.0.0:8888
'''

This will run the web application for monitoring logs in http://ip_address:8888/
This is the temporary decision. If you want to full time work mode - use nginx and uwsgi.
