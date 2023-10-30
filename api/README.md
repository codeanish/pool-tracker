Let me first track games

Game
Game Type
Player

Who breaks
Keep track of turns - how many balls did you pot?
Did you end your turn on a defensive shot or miss?
Who won?

DBML schema
```
Table game {
  id integer [primary key]
  player_1_id int
  player_2_id int
  breaking_player int
  winning_player int
  location varchar
  date datetime
}

Table players {
  id integer [primary key]
  name varchar
}



Ref: game.player_1_id > players.id

Ref: game.player_2_id > players.id

Ref: game.breaking_player > players.id

Ref: game.winning_player > players.id
```