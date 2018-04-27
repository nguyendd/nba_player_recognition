def parse(test):
	name = test.split(',')
	if len(name) > 1:
		return f"{name[1].strip()} {name[0]}"
	else: return name[0]



def getFormattedNbaPlayers():
	with open("all_active_nba_players.txt") as f:
		nbaPlayersWithLineBreak = f.readlines()

	unformmatedNbaPlayers = [nbaPlayerWithLineBreak.strip() for nbaPlayerWithLineBreak in nbaPlayersWithLineBreak]

	nbaPlayersList = []

	for nbaPlayer in unformmatedNbaPlayers:
		nbaPlayersList.append(parse(nbaPlayer))

	return nbaPlayersList
