import urllib.request, json
from clarifai.rest import ClarifaiApp
from parse import getFormattedNbaPlayers
import time
import os

key = os.getenv('GOOGLE_SEARCH_KEY')
cx = os.getenv('GOOGLE_SEARCH_CX')
clarifai_key = os.getenv('CLARIFAI_KEY')
numberOfResults = 9


# formattedNbaPlayers = getFormattedNbaPlayers()

app = ClarifaiApp(api_key=clarifai_key)

model = app.models.get('Nba Players')
#conceptIds = model.get_concept_ids()


# for conceptId in conceptIds:
# 	formattedConceptId = conceptId.replace(" ", "%20")
# 	print(formattedConceptId)
	#url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&num={numberOfResults}&searchType=image&q=lebron%20james"
	#r = urllib.request.urlopen(url)
	#json = json.loads(r.read())

#print(json.get('items')[0].get('link'))

# for nbaPlayer in formattedNbaPlayers:
# 	if not (nbaPlayer in conceptIds):
# 		model.add_concepts([nbaPlayer])
# 		time.sleep(1)


url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&num={numberOfResults}&searchType=image&q=Alex%20Abrines"
r = urllib.request.urlopen(url)
json = json.loads(r.read())
googleImageSearchItems = json.get('items')
imageLinks = list(map(lambda item: item.get('link'), googleImageSearchItems))

for imageLink in imageLinks:
	app.inputs.create_image_from_url(url=imageLink, concepts=['Alex Abrines'])


model.train()	