Starter
===================
![Django 1.8.4](http://img.shields.io/badge/Django-1.8.4-0C4B33.svg)
[![MIT License](https://img.shields.io/cocoapods/l/AFNetworking.svg)](http://opensource.org/licenses/MIT)

Starter is fully customized djanto stratproject template. It is built with [Python][2] using the [Django Web Framework][1].

Create Your Project
-------------
*Prerequisites: Django*

to create a new Django project, run the following command replacing PROJECT_NAME with your actual project name:

    $ django-admin.py startproject --template=https://github.com/LordK1/Starter  --extension=py,rst,md,txt,html,json <project_name>

Afterwards please reference the actual `README.md` you just created in your new project folder, all the references to "{{ project_name }}" will be changed accordingly.

-----

Make virtual environments
-------------------------

*Prerequisites: virtualenv, virtualenvwrapper*

    cd {{ project_name }}
    mkvirtualenv {{ project_name }}-dev && add2virtualenv `pwd`
    mkvirtualenv {{ project_name }}-prod && add2virtualenv `pwd`
    mkvirtualenv {{ project_name }}-test && add2virtualenv `pwd`


Install python packages
--------------------
For development:

    workon {{ project_name }}-dev
    sudo pip install --upgrade pip
    sudo pip install --upgrade setuptools
    sudo pip install -r requirements/dev.txt

For production:

    workon {{ project_name }}-prod
    sudo pip install --upgrade pip
    sudo pip install --upgrade setuptools
    sudo pip install -r requirements.txt

For testing:

    workon {{ project_name }}-test
    sudo pip install --upgrade pip
    sudo pip install --upgrade setuptools
    sudo pip install -r requirements/tmp.txt

Install bower packages
---------------------

*Prerequisites: bower*

    bower install

[django-bower][7] used for install many many other forntend frameworks like [bootstrap][8], [animation.css][12] and etc .
this command create and install all used dependencies defined in bower.json into components directory .

Create local postgres database for dev
--------------------------------------

*Prerequisites: Postgres and Heroku Toolbelt*

Install Postgres for your OS [here](http://www.postgresql.org/download/). For Max OSX the easiest option is to download and run [Postgres.app](http://postgresapp.com/).

    # Make sure Postgres.app is running
    workon {{ project_name }}-dev
    createdb {{ project_name }}-dev
    foreman run django-admin.py migrate

Refrences
-------------

1. Tanks and Inspired by
2. Two Scoops of Django 1.8 [Book][9][django-two-scoops-project][8]
3. alot of tanks from [django-kevin][4] very helpful documentions in  
4. [Caktus][2] website and [repository][5] very helpful package in
5. [The Twelve Factors][6]
6. [django-bower][10] 
7. [django-environ][11]

--------------------
#### <i class="icon-file"></i> Create a document



  [1]: https://www.djangoproject.com/
  [2]: https://www.python.org/
  [3]: https://www.caktusgroup.com/
  [4]: https://github.com/imkevinxu/django-kevin
  [5]: https://github.com/caktus/django-project-template
  [6]: http://12factor.net/
  [7]: https://github.com/nvbn/django-bower
  [8]: http://getbootstrap.com/
  [9]:http://twoscoopspress.org/products/two-scoops-of-django-1-8
  [10]:https://django-bower.readthedocs.org/en/latest/
  [11]:http://django-environ.readthedocs.org/en/latest/
  [12]:https://daneden.github.io/animate.css/
  


