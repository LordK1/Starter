Starter
===================
![Django 1.8.4](http://img.shields.io/badge/Django-1.8.4-0C4B33.svg)
[![MIT License](https://img.shields.io/cocoapods/l/AFNetworking.svg)](http://opensource.org/licenses/MIT)
[![Bower](https://img.shields.io/bower/v/bootstrap.svg)]()
[![PyPI](https://img.shields.io/pypi/wheel/Django.svg)]()
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]()

Starter is fully customized django stratproject template. It is built with [Python][2] using the [Django Web Framework][1].

Create Your Project
-------------
*Prerequisites: Django*

to create a new Django project, run the following command replacing PROJECT_NAME with your actual project name:

    $ django-admin.py startproject --template=https://github.com/LordK1/Starter/archive/master.zip  --extension=py,rst,md,txt,html,json,env <project_name>

Afterwards please reference the actual `README.md` you just created in your new project folder, all the references to "{{ project_name }}" will be changed accordingly.

-----

Make virtual environments
-------------------------

*Prerequisites: virtualenv, virtualenvwrapper*

    cd {{ project_name }}
    mkvirtualenv {{ project_name }}-dev && add2virtualenv `pwd`
    mkvirtualenv {{ project_name }}-prod && add2virtualenv `pwd`


Install python packages
--------------------
For development:

    workon {{ project_name }}-dev
    sudo pip install --upgrade pip
    sudo pip install --upgrade setuptools
    sudo pip install -r requirements/tmp.txt

For production:

    workon {{ project_name }}-prod
    sudo pip install --upgrade pip
    sudo pip install --upgrade setuptools
    sudo pip install -r requirements.txt


Install bower packages
---------------------

*Prerequisites: bower*

    bower install

[django-bower][7] used for install many many other forntend frameworks like [bootstrap][8], [animation.css][12] and etc .
this command create and install all used dependencies defined in bower.json into components directory .

Create local postgres database for dev
--------------------------------------

*Prerequisites: Postgresql*

Install Postgres for your OS [here](http://www.postgresql.org/download/).

    # Make sure Postgres.app is running
    workon {{ project_name }}-dev
    createdb {{ project_name }}-DB
    
  
Configurate env file
--------------------
Before you could be able to run and test project locally, should make configrate local.env file in settings folder 
	
	# Goto `project_name` folder and then settings folder
	cd project_name/settings/
	# Move local.sample.env into local.env
	mv local.sample.env local.env
	# Custom environment variables with your values
	gedit local.env



Run project locally in dev environment
--------------------------------------
For your easiest way make runnabel manage.py as terminal script with command 
	
	cd project_name
	sudo chmod 755 manage.py 
	enter your password
	# Then use runserver command 
	./manage.py runserver 

you should see output like below 

> Performing system checks...
> 
> System check identified no issues (0 silenced).
> 
> You have unapplied migrations; your app may not work properly until
> they are applied. Run 'python manage.py migrate' to apply them.
> 
> August 29, 2015 - 12:02:33 Django version 1.8.4, using settings
> 'FullishTask.settings.development' Starting development server at
> http://127.0.0.1:8000/ Quit the server with CONTROL-C.



---------------------------------------------------------------------------------
Refrences
-------------
1. Tanks and Inspired by
2. Two Scoops of Django 1.8 [Book][9][django-two-scoops-project][8]
3. alot of tanks from [django-kevin][4] for helpful documentions in  
4. [Caktus][2] website and [repository][5] for very helpful packages
5. fully helpful documentions on [django-extesion][13]
6. [The Twelve Factors][6]
7. [django-bower][10] 
8. [django-environ][11]


[1]: https://www.djangoproject.com/
[2]: https://www.python.org/
[3]: https://www.caktusgroup.com/
[4]: https://github.com/imkevinxu/django-kevin
[5]: https://github.com/caktus/django-project-template
[6]: http://12factor.net/
[7]: https://github.com/nvbn/django-bower
[8]: http://getbootstrap.com/
[9]: http://twoscoopspress.org/products/two-scoops-of-django-1-8
[10]:https://django-bower.readthedocs.org/en/latest/
[11]:http://django-environ.readthedocs.org/en/latest/
[12]:https://daneden.github.io/animate.css/
[13]:http://django-extensions.readthedocs.org/en/latest/