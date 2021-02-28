# Telegram bot for post matches from HLTV
## Features
* Parsing and store Matches
* Country filter
* Send to telegram

## Install 
* Create and fill .env from .env.example
* Run `alembic upgrade head`
* Get service_key.json and store it to project https://stackoverflow.com/questions/56875958/how-to-authenticate-docker-container-with-google-service
## Migrations
How to create

`alembic revision --autogenerate -m "Migration name"`

How to apply migrations

`alembic upgrade head`

## Testing 
`python -m unittest discover -p '*Test.py'`
