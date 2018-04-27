#nba_players_file = open("NBA_Facial_Recognition/all_active_nba_players.txt", "r")
#nbaPlayersWithLineBreak = nba_players_file.readLines()
#nbaPlayers = [nbaPlayersWithLineBreak.rstrip('\n'\) for nbaPlayersWithLineBreak in open("NBA_Facial_Recognition/all_active_nba_players.txt")]
#print(nbaPlayers)
import urllib.request, json
from clarifai.rest import ClarifaiApp
from parse import getFormattedNbaPlayers
import time
import os

key = os.getenv('GOOGLE_SEARCH_KEY')
cx = os.getenv('GOOGLE_SEARCH_CX')
clarifai_key = os.getenv('CLARIFAI_KEY')
numberOfResults = 5
url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&num={numberOfResults}&searchType=image&q=lebron%20james"
r = urllib.request.urlopen(url)
json = json.loads(r.read())

print(json.get('items')[0].get('link'))

formattedNbaPlayers = getFormattedNbaPlayers()

app = ClarifaiApp(api_key=clarifai_key)

model = app.models.get('Nba Players')
conceptIds = model.get_concept_ids()



for nbaPlayer in formattedNbaPlayers:
	if not (nbaPlayer in conceptIds):
		model.add_concepts([nbaPlayer])
		time.sleep(1)