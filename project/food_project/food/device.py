from tdm.lib.device import  DddDevice, DeviceWHQuery
from urllib2 import Request,urlopen
import json
import requests
#import spoonacular as sp



class FoodDevice(DddDevice):

    key = "94ef1f7a2b9941a1a9a315b35a7d5f40"
    def getRecipeData(self,query,cuisine=None,diet=None,meal_type=None,intolerances=None,exclude_ingredients=None):
        url = "https://api.spoonacular.com/recipes/search?apiKey={}".format(self.device.key)
        param = {
            "query": query,
            "cuisine": cuisine,
            "diet": diet,
            "meal_type": meal_type,
            "intolerances": intolerances,
            "exclude_ingredients":exclude_ingredients          
        }
        # url = "https://api.spoonacular.com/recipes/search?apiKey={}query={}&cuisine={}&diet={}&meal_type={}&intolerances={}".format(self.device.key,query,cuisine,diet,meal_type,intolerances)

        print(url)
        print(param)
        response = requests.get(url, params=param)
        #request = Request(url)
        #response = urlopen(request)
        data = response.read()
        return json.loads(data)
    
    
    def getIngredientsData(self,recipe_id):
        url = "https://api.spoonacular.com/recipes/{}/?apiKey={}".format(recipe_id, self.device.key)
        print(url)
        request = Request(url)
        response = urlopen(request)
        data = response.read()
        return json.loads(data)

    class detailed_recipe(DeviceWHQuery):
        def perform(self,query,cuisine,diet,meal_type,intolerances,exclude_ingredients=None):
            recipe_data = self.device.getRecipeData(query,cuisine,diet,meal_type,intolerances,exclude_ingredients=None)
            first_recipe_id = recipe_data.results[0].id
            #first_recipe = data.results[0]
            first_recipe_title = recipe_data.results[0].title

            ingredients_data = self.device.getIngredientsData(first_recipe_id)
            ingredients_list = []
            ingredients= ingredients_data.extendedIngredients
            for ing in ingredients:
                print(ing)
                ingredients_list.append(ing)
            ingredients_str = ', '.join(ingredients_list)

            return [first_recipe_title. ingredients_str]

    class simple_recipe(DeviceWHQuery):
        def perform(self,query,cuisine=None,diet=None,meal_type=None,intolerances=None,exclude_ingredients=None):
            recipe_data = self.device.getRecipeData(query,cuisine=None,diet=None,meal_type=None,intolerances=None,exclude_ingredients=None)
            first_recipe_id = recipe_data.results[0].id
            first_recipe_title = recipe_data.results[0].title

            ingredients_data = self.device.getIngredientsData(first_recipe_id)
            ingredients_list = []
            ingredients= ingredients_data.extendedIngredients
            for ing in ingredients:
                print(ing)
                ingredients_list.append(ing)
            ingredients_str = ', '.join(ingredients_list)
            
            return [first_recipe_title. ingredients_str]