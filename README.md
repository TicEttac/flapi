# FLAPI
## Description

This project is a basic Django REST framework api made as a leaderboard server for [this flappy bird repository](https://github.com/TicEttac/Flappy_Bird_Godot). It got 2 endpoints which are used to get leaderboard and set your high score.

## Endpoints
### GET leaderboard

- 127.0.0.1:8000/leaderboard - Used to get leaderboard as a list of pair user/score (eg: [{"pseudo":string, "score":int}])

### POST high score

- 127.0.0.1:8000/score/ - Used to post your own high score

##Usage

```bash
$>git clone https://github.com/TicEttac/flapi.git

$>cd flapi

$>source env/bin/activate

$>cd flapi

$>./manage.py runserver
```

## Author

Niels SAUVIGNON

Github : https://github.com/TicEttac

## Licence

This project is distributed under MIT licence. See LICENSE.md
