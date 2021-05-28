import decoder, config, os, json

from datetime import datetime

tstart = datetime.now()

players_list = {}

if not config.replays_path.endswith("/"):
    config.replays_path = f'{config.replays_path}/'

def ext_check(replay):
    if replay.endswith(".wotreplay"):
        return True

filtered = filter(ext_check, os.listdir(config.replays_path))

c = 0

for r in filtered:
    c += 1

    replay = decoder.replay(f'{config.replays_path}{r}',7)
    
    playerName = replay["playerName"]

    for player in replay["vehicles"]:
        name = replay["vehicles"][player]["name"]
        if name in players_list:
            players_list[name] += 1
        else:
            players_list[name] = 1

    players_list.pop(playerName)

players_list = dict(sorted(players_list.items(), key=lambda x: (-x[1], x[0])))

with open('players.json', 'w') as out:
    json.dump(players_list, out)

tend = datetime.now()

delta = tend - tstart
ms = round(delta.seconds * 1000 + delta.microseconds / 1000, 2)

top5 = list(players_list.items())[0:5]
text = ""
i = 1

for e in top5:
    listed = list(e)
    text += f'[{i}] {listed[0]} ({listed[1]} times)\n'
    i += 1

print(f'Parsed {c} replays in {ms}ms')
print(f'\nTop 5 :\n{text}')