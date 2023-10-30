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

## Next steps
Add the ability to edit players
Add the ability to declare a winner of a game
Add the ability to set who breaks from the creation of a game