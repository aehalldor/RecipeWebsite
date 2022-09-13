import requests
import json
parameters = {
    "f": "a"
}
response = requests.get("http://www.themealdb.com/api/json/v1/1/search.php",  params=parameters)
#print(response.status_code) ##responds 200 if successful
#print(response.json()) ##prints the recipe bc of Arrabiata search
def jprint(obj):
	text = json.dumps(obj, sort_keys=True, indent=4)
	print(text)

# jprint(response.json()['meals']['strInstructions'])

mealInstr = response.json()['meals']
names = []
imgs = []
for d in mealInstr:
	k = d['strMeal']
	l = d['strMealThumb']
	names.append(k)
	imgs.append(l)

