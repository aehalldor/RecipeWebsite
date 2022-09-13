import requests

def fillSearch():
    parameters = {
    "s": query
    }
    response = requests.get("http://www.themealdb.com/api/json/v1/1/search.php",  params=parameters)

def search(query):
    parameters = {
    "s": query
    }
    response = requests.get("http://www.themealdb.com/api/json/v1/1/search.php",  params=parameters)


    mealInstr = response.json()['meals']
    names = []
    imgs = []
    for d in mealInstr:
        k = d['strMeal']
        l = d['strMealThumb']
        names.append(k)
        imgs.append(l)

