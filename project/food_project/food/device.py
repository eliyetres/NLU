from tdm.lib.device import  DddDevice, DeviceWHQuery
from urllib2 import Request,urlopen
import json
import requests

class FoodDevice(DddDevice):

    key = "94ef1f7a2b9941a1a9a315b35a7d5f40"
    def getRecipeData(self,query,cuisine,diet,meal_type,intolerances):
        print(query, cuisine,diet,meal_type,intolerances)
        url = "https://api.spoonacular.com/recipes/search?apiKey={}".format(self.key)
        params = {
            "query": query,
            "cuisine": cuisine,
            "diet": diet,
            "meal_type": meal_type,
            "intolerances": intolerances       
        }
        # url = "https://api.spoonacular.com/recipes/search?apiKey={}query={}&cuisine={}&diet={}&meal_type={}&intolerances={}".format(self.device.key,query,cuisine,diet,meal_type,intolerances)

        print(url)
        print(params)        
        response = requests.get(url, params=params)
        print(response.json)
        return response.json()
   
    
    def getIngredientsData(self,recipe_id):
        url = "https://api.spoonacular.com/recipes/{}/information?apiKey={}".format(recipe_id, self.key)
        print(url)
        request = Request(url)
        response = urlopen(request)
        data = response.read()
        return json.loads(data)

    class detailed_recipe(DeviceWHQuery):
        def perform(self,query,cuisine,diet,meal_type,intolerances):
            recipe_data = self.device.getRecipeData(query,cuisine,diet,meal_type,intolerances)          
            # If response returns no recipes, return string
            if len(recipe_data['results']) >= 0:
                return ["Sorry, no recipes found."]

            first_recipe = recipe_data['results'][0]
            first_recipe_id = first_recipe['id']          
            first_recipe_title = first_recipe['title']           

            ingredients_data = self.device.getIngredientsData(first_recipe_id)
            ingredients_list = []
            ingredients= ingredients_data['extendedIngredients']
            for i in range(len(ingredients)):
                name = ingredients[i]['name']
                amount = str(int(ingredients[i]['amount']))
                unit  = ingredients[i]['unit']
                ing_str = amount+" "+unit+" "+name
                print(ing_str)
                ingredients_list.append(ing_str)
            ingredients_str = ', '.join(ingredients_list)

            print("\n DETAILED RECIPE")
            print("------------------")
            print("FIRST RECIPE")
            print("------------------------------------------")
            print(first_recipe_title)
            print(ingredients_str)

            #return [first_recipe_title, ingredients_str]
            return [ingredients_str]

    class simple_recipe(DeviceWHQuery):
        def perform(self,query,cuisine,diet,meal_type,intolerances):
            recipe_data = self.device.getRecipeData(query,cuisine,diet,meal_type,intolerances)
            # first_recipe_id = recipe_data.results[0].id
            # first_recipe_title = recipe_data.results[0].title

            # ingredients_data = self.device.getIngredientsData(first_recipe_id)
            # ingredients_list = []
            # ingredients= ingredients_data.extendedIngredients
            # for ing in ingredients:
            #     print(ing)
            #     ingredients_list.append(ing)
            # ingredients_str = ', '.join(ingredients_list)
            
            # return [first_recipe_title, ingredients_str]
            return ["test"]