
import openai
import os
import re 


class Recipe():
    def __init__(self):
        self.ingredients = []
        self.recipe_title = ""
        self.prompt = ""
        self.ingredients_string = ""
        self.response = ""
        
    def add_ingredient(self):
        while True:
            ingredient = input("Enter ingredient name (enter 'q' to quit): ")
            if ingredient == 'q':
                break
            else:
                self.ingredients.append(ingredient)
    
    def create_recipe_prompt(self):
         self.ingredients_string = ', '.join(self.ingredients)
         self.prompt = f"Create a detailed recipe based on only the following ingredients (Assume user has basic cooking ingredients): {self.ingredients_string}\n"\
            +f"Additionally, assign a title starting with 'Recipe Title: ' to the recipe."
            
    def create_recipe(self):
        self.response = openai.Completion.create(
            engine="text-davinci-003",
            max_tokens=256,
            prompt=self.create_recipe_prompt(),
            temperature=0.7,)
    
    def get_recipe_title(self):
        recipe_text = self.response.choices[0].text
        self.recipe_title = re.findall(r"Recipe Title: (.*)", recipe_text, re.MULTILINE)[0].strip().split('Recipe Title: ')[-1]
        return self.recipe_title
    
    
        
        
                    

            