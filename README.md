# heroquest-stats-tracker

A stats tracker for the HeroQuest board game.

## Getting Started

Clone the repository and move into the project directory:
```
$ git clone https://github.com/kappq/heroquest-stats-tracker.git
$ cd heroquest
```

Create and activate a virtual environment:
```
$ python -m venv venv
$ source venv/bin/activate
```

Install the requirements:
```
$ pip install -r requirements.txt
```

Rename the `.env.template` to `.env` and edit the configuration:
```
$ mv .env.template .env
$ nano .env
```

Create the database tables:
```
$ python
Python 3.12.3 (main, Apr 23 2024, 09:16:07) [GCC 13.2.1 20240417] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from heroquest import db, create_app, models
>>> app = create_app()
>>> with app.app_context():
...     db.create_all()
```

Run the application:
```
$ flask --debug --app=heroquest run
```
