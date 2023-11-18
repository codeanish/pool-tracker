# pool-tracker
An app to let you track practice sessions for pool (not swimming)


## Design

Postgres database to store practice sessions
Python/FastAPI api to interact with DB
React UI

## Database design
Want to store games
Each game has 2 players
Track each turn:
* how many balls did the player taking the turn pot?
* Did they finish up on a safety shot or a miss or run out?

Initially 3 tables

Players - Who plays
Games - Wrapper for a collection of turns
Turns - How many turns

## Database Migrations with Alembic
As the model is incremented, we're going to run an alembic migration to take the following steps:

1. Create a migration script
2. Apply the migration to the database

The creation of the migration script happens in the code editor using the command

> alembic revision --autogenerate -m "Message"

In order to create a revision, we need to point it to a live version of the database by ensuring it has the correct database URL. This is currently done through environment variables in the database.py script.

Once the migration script has been created, I've baked in the application of the migration to the docker compose process. As the api container comes up, it applies any new migrations to the database. A version number is stored in the database to track the database version, and is changed every time there is a new version.

## Next steps
* Complete create token API
* Add a verify user token API
* Use private key for creating a token
* Use public key for decoding a token
* Add the ability to edit players
* When creating a game, validate that the players exist
* Add the ability to declare a winner of a game
