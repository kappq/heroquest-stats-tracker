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
$ python create_tables.py
```

Run the application:
```
$ flask --debug --app=heroquest run
```
