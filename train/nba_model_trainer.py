import urllib.request, json
from clarifai.rest import ClarifaiApp
from parse import getFormattedNbaPlayers
import time
import os

key = os.getenv('GOOGLE_SEARCH_KEY')
cx = os.getenv('GOOGLE_SEARCH_CX')
clarifai_key = os.getenv('CLARIFAI_KEY')
numberOfResults = 10


# formattedNbaPlayers = getFormattedNbaPlayers()

app = ClarifaiApp(api_key=clarifai_key)

model = app.models.get('Nba Players')
#conceptIds = model.get_concept_ids()

untrainedConcepts = ['Bradley Beal', 'John Wall', 'Quincy Acy', 'Steven Adams']

for conceptId in untrainedConcepts:
	formattedConceptId = conceptId.replace(" ", "%20")
	url = f"https://www.googleapis.com/customsearch/v1?key={key}&cx={cx}&num={numberOfResults}&searchType=image&q={formattedConceptId}"
	r = urllib.request.urlopen(url)
	json_data = json.loads(r.read())
	googleImageSearchItems = json_data.get('items')
	imageLinks = list(map(lambda item: item.get('link'), googleImageSearchItems))
	for imageLink in imageLinks:
		app.inputs.create_image_from_url(url=imageLink, concepts=[conceptId])
		time.sleep(2)

#print(json.get('items')[0].get('link'))

model.train()	