# 3MW Application task

Web Application built with Django

## Getting Started

### Prerequisites

Install the following software on your PC
- Python 2.7.X
- Git

### Installation 

1. Clone the repository `$ git clone <path to repository>` and `$ cd` into it
2. Run `$ pip install -r requeriments.txt`

### Setup the environment

Before launching the application from your local webserver or from the Django command-line utility, please take your time to setup the environment.

You should try hard not to put any license key, password or any other parameter that is used by any service or API, use the separate settings file for your environment.

Take a look at the folder `3MW/settings`, there you can find a list of files that will target an specific environment. Just take one file, say development.py.txt and save it as `development.py`.

This file should inherit all settings from 3MW/settings/base.py, and override specifics settings when needed.

```bash
$ export DJANGO_SETTINGS_MODULE=App3MW.settings.development
$ python manage.py runserver
.
.
Django version 1.11, using settings 'App3MW.settings.development'
```
### Setup database

1. run `$ mkdir data`
2. run `$ python manage.py migrate`

### Start the application

You may start the application with the following command

```bash
$ python manage.py runserver
.
.
Django version 1.11, using settings 'App3MW.settings.development'
```

### Populate the database with test data

You might be able to create some testing data, by running the following command.

```bash
$ python manage.py test_data
.
.
```
