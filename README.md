Django-sass-babel-gulp boilerplate
======
Author: [Max Saykov](https://github.com/iviaks/)

What's included?
------
- [Django v1.11.5](https://docs.djangoproject.com/en/1.11/)
- Python 3.5 based [Dockerfile](https://hub.docker.com/_/python/)
- Node 8 [docker image](https://hub.docker.com/_/node/)
- [Docker compose](https://docs.docker.com/compose/)
- [Gulp](https://gulpjs.com/)
- [Sass](http://sass-lang.com/)
- [Babel](https://babeljs.io/)
- [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
- Postgresql 9.6 database
- Template structure

How to setup project?
------
1. Run `python setup.py`

How to run project?
------
1. Setup .env file according to .env.example
2. Build project `docker-compose build`
3. Run database `docker-compose up -d database`
4. Run node installing `docker-compose run frontend yarn`
5. Run project `docker-compose up`

Project Structure
------
* **./backend/** Django web server
* **./frontend/** Main frontend folder
  * **./assets/** Assets folder
    * **./js/** Javascript (including ES2015 syntax)
    * **./scss/** Sass
    * **./fonts/** Fonts
    * **./images/** Images
  * **./dist/** Results folder

Are you having any question?
------
Email: max-saykov@mail.ru
