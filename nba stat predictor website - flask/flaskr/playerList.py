import os.path

pathname = "/Users/pranav/Downloads/nba stat predictor website - flask/flaskr/players.txt"

allPlayers = []
if os.path.isfile(pathname):
    file = open(pathname, 'r')
    allPlayers = file.read().splitlines()
    file.close()

for player in allPlayers:
    b = '<option value = "{}">'.format(player)
    print(b)
