# Development Guide

## Basic Information
LingoMap is authored in Python 3.5, using framework Django 1.9. It should work with all DBMS compatible with Django's ORM, including SQLite, MySQL, and Postgres.

## Folder Structure
The Git repository currently contains only one directory, `server`, in which the project resides. It is intended that other components, e.g. integration with other projects, reside in other folders alongside `server`.

Folder `server` contains the server as a standard Django project.

## Setting up Development Environment
It is strongly recommended to install LingoMap in a `virtualenv` box. This will help ensure dependencies do not clash with other projects.

It is recommended not to check in the virtual environment into repository, mostly because `virtualenv` are not portable, and therefore checking it in may in fact bring more problem than it solves.

The following guide has been written with OS X in mind. Details likely will differ on Linux or Windows.

### Installing Python
LingoMap is written in Python 3.5. While so far it has not used any explicit Python 3 feature yet, the clear separation between strings and byte streams have been highly beneficial. The code likely will not run properly in Python 2. Most OS however, by default, only provide Python 2. On OS X, the easiest way to install Python 3 is either via [Homebrew](http://brew.sh/) or via [pyenv](https://github.com/yyuu/pyenv). In subsequent steps, when creating `virtualenv`, make sure Python 3 is used.

### Developing with PyCharm
It is highly recommended to use PyCharm for development. It offers excellent support for Django projects, providing developer ergonomics features such as autocomplete, refactoring, database viewer, and more.

PyCharm has built-in support for `virtualenv`, and one should creating a dedicated environment for LingoMap before proceeding. In Preferences -> Project Interpreter, by pressing the gear button, one can create a new `virtualenv`.

Then, to create the PyCharm project, one can simply open the `server` folder.

The project will not run without dependencies, the most obvious one being Django. A `requirements.txt` is provided, and one can configure PyCharm to use it by following guide [here](https://www.jetbrains.com/help/pycharm/2016.1/creating-requirement-files.html).

Afterwards, running the project is as easy as clicking the run button.

### Developing without IDE
It is possible to develop LingoMap without IDE as well. 

First one would need to create a `virtualenv`. Once the environment is activated, dependencies need to be satisfied using `pip install -r requirements.txt`. Then, one should be able to run the project using `python manage.py runserver 8000`

### Prepare Database
Before the website can run, database must be properly populated. Run `python manage.py makemigrations` will generate the necessary migrations, and `python manage.py migrate` will populate the database. These steps should be redone whenever the database schema is modified.

### Create admin user
It goes without saying that a superuser must be created to administer the website. Running `python manage.py createsuperuser` will do this for you.

## Code Structure
LingoMap is a standard Django project, consisting of several relatively independent apps. 

#### `badges`
Supports the badge system

#### `common`
Common reusable functionalities, including models, template tags, etc.

#### `dashboard`
User dashboard

#### `home`
Home page. Mostly just a static page.

#### `resources`
Resources.

#### `image_cropping`
This is a vendored [django-image-cropping](https://github.com/jonasundderwolf/django-image-cropping) project, heavily modified to support cropping when adding a new entry.

There are several other top level directories as well, including

#### `templates`
Stores templates that don't belong to specific apps, including general layout and user account management

#### `static`
Static resources, including CSS, JavaScript, images, etc.