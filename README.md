Django-gulp boilerplate
======
Author: [Max Saykov](https://github.com/iviaks/)

What's included?
------
- [Django v1.11.5](https://docs.djangoproject.com/en/1.11/)
- [Django Rest Framework](http://www.django-rest-framework.org/)
- [Graphene-Python](http://graphene-python.org/)
- Python 3.5 based [Dockerfile](https://hub.docker.com/_/python/)
- Node 8 [docker image](https://hub.docker.com/_/node/)
- [Docker compose](https://docs.docker.com/compose/)
- [Gulp](https://gulpjs.com/)
- [Sass](http://sass-lang.com/)
- [Stylus](http://stylus-lang.com/)
- [Babel](https://babeljs.io/)
- Postgresql 9.6 database
- Template structure

How to setup project?
------
1. Run `python setup.py`
2. Setup .env file according to .env.example
3. Build project `docker-compose build`
4. Run twice database container `docker-compose up -d database`
    * Enter to database bash `docker-compose run database bash`
    * Create user according to .env file `createuser --interactive -P -s`
    * Create database according to .env file `createdb <dbname> -O <username>`
    * Leave database container `exit`
5. Install node dependencies `docker-compose run frontend yarn`
6. Run backend `docker-compose run backend bash`
    * Run migrations `python manage.py migrate`
    * Leave backend container `exit`

How to run project?
------
```bash
docker-compose up
```

Project Structure
------
* **./backend/** Django web server
* **./frontend/** Main frontend folder
  * **./assets/** Assets folder
    * **./js/** Javascript (including ES2015 syntax)
    * **./scss/** Sass
    * **./styl/** Stylus
    * **./fonts/** Fonts
    * **./images/** Images
  * **./dist/** Results folder

Are you having any question?
------
Email: max-saykov@mail.ru
