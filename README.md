# WoT Players meeting counter

Made with ![python](https://img.shields.io/badge/python-3.9-blue?link=https://www.python.org/downloads/)

[![GitHub stars](https://img.shields.io/github/stars/LockBlock-dev/wot-replays-users-met-counter.svg)](https://github.com/LockBlock-dev/wot-replays-users-met-counter/stargazers)

The purpose of this script is to provide you a list of all the players you have met in your saved games (replays).


## How to use

• Download [Python](https://www.python.org/downloads/)

• Download the project or clone it

• Edit the [config](./config.py) :
```python
##Path to your WoT replays folder (or any folder that contains replays)
replays_path = "C:/Games/World_of_Tanks_EU/replays/"
```

• Run the python script in a command prompt :
```bash
python parser.py
```
or
```bash
python3 parser.py
```

• The full list is available in [players](./players.json)

• The command prompt prints you the amount of replays, the elapsed time and the top 5 of players you have met.


## Credits

[Decoder made by Phalynx](https://github.com/Phalynx/wotdecoder/blob/master/wotdecoder.py).


## Copyright

See the [license](/LICENSE).