# logs4free
Display logs from web server log files (apache, nginx) in your browser in real time mode.
It consists of two independent parts. One of them collect, parse and store web server logs in mysql database table.
Second one is a web application to display that logs in real time mode using ajax.
It's means, that you can watch you server logs in you browser.


## INSTALL

### Install python and django
[django](https://docs.djangoproject.com/en/1.8/intro/install/)


### Install python mysqldb connector
[mysqldb connector](http://mysql-python.sourceforge.net/MySQLdb.html#installation)


### Install mysql
[mysql](http://dev.mysql.com/doc/refman/5.7/en/installing.html)


### Create database for logs storing
`CREATE DATABASE `log4free` CHARACTER SET utf8 COLLATE utf8_general_ci;`


## SETTINGS

### Export django-settings-module to environments variables

From your logs4free directory:
`export DJANGO_SETTINGS_MODULE=log4free.settings`

### Database password
Specify database password in `logs4free/log4free.settings.py` file. You can find the customize marker there.


## USAGE

### Start the logs storing

From your logs4free directory:
`python tailer.py /var/log/apache2/access.log &`

This will run the logs storage process in background mode. You can use other path for logs location.

### Start the web app
From your logs4free directory:
`python manage.py runserver 0.0.0.0:8888`

This will run the web application for monitoring logs in `http://ip_address:8888/`
This is the temporary decision. If you want to full time work mode - use nginx and uwsgi.
