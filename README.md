Fyyur Project
-----

### How to setup
First of all you have to make sure that your postgres server is running with the following command:

```$ pg_ctl -D /usr/local/var/postgres start```

Now you have to create a database with the name `fyyur`:

```$ createdb fyyur```

Make sure you have Flask installed:

```$ sudo pip3 install Flask```

Initialize and activate a virtualenv:

```
$ cd fyyur
$ virtualenv --no-site-packages env
$ source env/bin/activate
```

Install the dependencies:

```$ pip install -r requirements.txt```

Now make sure you have Flask-Migrate and Flask-Script installed:

```
$ pip3 install Flask-Migrate
$ pip3 install Flask-Script
```

Now setup your database to use our schema that is defined in `app.py`:

```
flask db upgrade
```

Run the development server:

```
$ export FLASK_APP=myapp
$ export FLASK_ENV=development # enables debug mode
$ python3 app.py
```

Navigate to Home page http://localhost:5000