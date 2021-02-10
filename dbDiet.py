import json
from nutritionix import Nutritionix
from datetime import date
import csv

nix = Nutritionix(app_id="38d23567", api_key="b61b0e6e70b4d263450c3f13b442affd")

"""
ORDER TO RUN THIS CLASS
    - initialize class
    - Run setDataValues function and input necessary data
    - Run input_json_db function to create create structure of data to be added or appended and save that data in a variable
    - Goes the functions from the api
"""

class dbDiet():
    def __init__(self):
        self.id_meal =  1 #self.setIdMeal()
        self.solid_liquid = True #true == solid
        self.weather = self.setWeather("Mérida, MX") 
        self.date = self.setDate()
        self.hour = 12
        self.like_dislike = True
        self.meal_name = "none"
        self.ingredients = "none"
        self.item_id = "none"
    

    # SETTERS
    def setIdMeal(self):
        with open("db_diet.csv") as db:
            reader = csv.reader(db, delimiter=',')
            counter = 0
            for i in reader:
                counter += 1
            self.id_meal = counter

    def setSolidLiquid(self, state):
        self.solid_liquid = state
    
    def setWeather(self, city):
        import requests
        weather_api_key = "b8e855d7f86daab2e01a4c46afc9cc94"
        b_url = "http://api.openweathermap.org/data/2.5/weather?"
        url = b_url + "appid=" + weather_api_key + "&q=" + city
        response = requests.get(url)
        x = response.json()
        if x["cod"] != "404":
            y = x["main"]
            return float('{:.2f}'.format(y['temp']-273))   
    
    def setDate(self):
        d = date.today()
        return d.strftime("%d/%m/%Y")

    def setHour(self, x):
        self.hour = x

    def setLikeDislike(self,ld):
        self.like_dislike = ld

    def setMealName(self,mn):
        self.meal_name = mn
    
    def setIngredients(self, ingre):
        self.ingredients = ingre

    def setItemId(self, itd):
        self.item_id = itd


    # GETTERS
    def getIdMeal(self):
        return self.id_meal
    def getSolidLiquid(self):
        return self.solid_liquid
    def getWeather(self):
        return self.weather
    def getDate(self):
        return self.date
    def getHour(self):
        return self.hour
    def getLikeDislike(self):
        return self.like_dislike
    def getMealName(self):
        return self.meal_name
    def getIngredients(self):
        return self.ingredients
    def getItemId(self):
        return self.item_id




    """GENERAL FUNCTIONS """
    def setDataValues(self):

        self.solid_liquid = bool(input("State of meal((solid == True) or (liquid==False)): "))
        self.hour = int(input("At what hour did you had your meal?: "))
        self.like_dislike = bool(input("Do you like or dislike your meal?(LIKE == True, DISLIKE==False): "))
        self.meal_name = input("What's the meal name?: ")

        meal_name_results = self.getSearchResults(self.meal_name)
        counter = 0
        print("INTRODUCE THE NUMBER OF YOUR OPTION:")
        for i in meal_name_results:
            print(counter,"->\tID: ", i[0], "\tNAME: ", i[1])
            counter+=1
        meal_menu = int(input("$option>> "))
        self.meal_name = meal_name_results[meal_menu][1]
        self.item_id = meal_name_results[meal_menu][0] 
        
        # special function for ingredients
        number_ingredients= int(input("how many ingredients does your meal have?: "))
        ingredients_info = [] # [ingredient name, quantity in grams]
        for i in range(number_ingredients):
            ingredient_name = input("\t- Ingredient name: ")
            ingredient_quantity = input("\t- Ingredient quantity: ")
            ingredients_info.append([ingredient_name, ingredient_quantity])
        
        self.setIdMeal()


    def getSearchResults(self, product): # This function returns all the finded products
        results  = nix.search(product).json()
        list_search_results = []
        for i in results["hits"]:
            list_search_results.append([i["fields"]["item_id"], i["fields"]["item_name"]])
        return list_search_results

    def getItemData(self, it): # Gets the data by the item id
        return nix.item(id=it).json()

    def createDataBase(self):
        with open("db_diet.csv", "w", newline='') as db:
            writer = csv.writer(db)
            writer.writerow(["id_meal", "solid/liquid", "weather",
                            "date", "hour", "like/dislike", "meal_name",
                            "ingredients", "item_id", "brand_name",
                            "nf_calories", "nf_calories_from_fat",
                            "nf_total_fat", "nf_saturated_fat", 
                            "nf_trans_fatty_acid", "nf_polyunsaturated_fat",
                            "nf_monounsaturated_fat", "nf_cholesterol", 
                            "nf_sodium", "nf_total_carbohydrate", 
                            "nf_dietary_fiber", "nf_sugars", "nf_protein", 
                            "nf_vitamin_a_dv", "nf_vitamin_c_dv", "nf_calcium_dv", 
                            "nf_iron_dv", "nf_refuse_pct", "nf_serving_weight_grams",
                            'allergen_contains_milk', 'allergen_contains_eggs',
                            'allergen_contains_fish', 'allergen_contains_tree_nuts',
                            'allergen_contains_peanuts', 'allergen_contains_wheat',
                            'allergen_contains_soybeans', 'allergen_contains_gluten'])

    def setDataToDataBase(self):
        local_variables = [self.id_meal, self.solid_liquid, self.weather,
                            self.date, self.hour, self.like_dislike, self.meal_name,
                            self.ingredients, self.item_id]
        api_variables = ["brand_name", "nf_calories", "nf_calories_from_fat",
                            "nf_total_fat", "nf_saturated_fat", 
                            "nf_trans_fatty_acid", "nf_polyunsaturated_fat",
                            "nf_monounsaturated_fat", "nf_cholesterol", 
                            "nf_sodium", "nf_total_carbohydrate", 
                            "nf_dietary_fiber", "nf_sugars", "nf_protein", 
                            "nf_vitamin_a_dv", "nf_vitamin_c_dv", "nf_calcium_dv", 
                            "nf_iron_dv", "nf_refuse_pct", "nf_serving_weight_grams",
                            'allergen_contains_milk', 'allergen_contains_eggs',
                            'allergen_contains_fish', 'allergen_contains_tree_nuts',
                            'allergen_contains_peanuts', 'allergen_contains_wheat',
                            'allergen_contains_soybeans', 'allergen_contains_gluten']
        
        ready_values_list = []
        
        for i in local_variables:
            #ready_values_list.append(self.id_meal)
            ready_values_list.append(i)
        y = self.getItemData(self.item_id)

        for i in api_variables:
            ready_values_list.append(y[i])
        with open("db_diet.csv", "a+", newline='') as db:
            writer = csv.writer(db)
            writer.writerow(ready_values_list)

    def automatic(self):
        self.setDataValues()
        self.setDataToDataBase()