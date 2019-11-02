from tdm.lib.device import  DddDevice, DeviceWHQuery
from urllib2 import Request,urlopen
import json
import requests

class FoodDevice(DddDevice):

    key = "94ef1f7a2b9941a1a9a315b35a7d5f40"
    def getRecipeData(self,query,cuisine,diet,meal_type,intolerances):
        print(query, cuisine,diet,meal_type,intolerances)
        # fulhack
        if cuisine == "no":
            cuisine = None
        if diet == "no":
            diet = None
        if meal_type == "no":
            meal_type = None
        if intolerances == "no":
            intolerances = None
        
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

    class recipe(DeviceWHQuery):
        def perform(self,query,cuisine,diet,meal_type,intolerances):
            recipe_data = self.device.getRecipeData(query,cuisine,diet,meal_type,intolerances)          
            # If response returns no recipes, return string
            if len(recipe_data['results']) == 0:
                return ["sorry, no recipes found"]

            first_recipe = recipe_data['results'][0]
            first_recipe_id = first_recipe['id']          
            first_recipe_title = first_recipe['title']           

            ingredients_data = self.device.getIngredientsData(first_recipe_id)
            ingredients_list = []
            ingredients= ingredients_data['extendedIngredients']
            for i in range(len(ingredients)):
                name = ingredients[i]['name']
                
                amount = ingredients[i]['amount']            
                if (amount).is_integer(): # format into int without floating point if eg. 1.0 dl
                    amount = str(int(amount))
                else:
                    amount= str(round(amount,1)) # if it's 1,5 dl, keep float
                unit  = ingredients[i]['unit']
                ing_str = amount+" "+unit+" "+name
                print(ing_str)
                ingredients_list.append(ing_str)
            ingredients_str = ', '.join(ingredients_list)

            print("------------------")
            print("RECIPE")
            print("------------------")
            print(first_recipe_title)
            print(ingredients_str)

            result_string = "The recipe for {} are {}.".format(first_recipe_title, ingredients_str)
            #return [first_recipe_title, ingredients_str]
            return [result_string]


    class ask_about_intolerances(DeviceWHQuery):
        def perform(self):
            return ["."]

    class ask_about_meal_type(DeviceWHQuery):
        def perform(self):
            return ["."]

    class ask_about_diet(DeviceWHQuery):
        def perform(self):
            return ["."]