import requests
import shutil 
import openai

class Image():
    def __init__(self):
        self.image_url = ""
        self.image_file_name = ""
        self.image_prompt = ""
        self.image_response = ""
    
    # Create a prompt for the recipe image based on the recipe title
    def create_image_prompt(self, recipe_title):
        self.image_prompt = f"{recipe_title}, professional food photography, 15mm, studio lighting"
    
    def create_image(self):
        self.image_response = openai.Image.create(
            prompt=self.image_prompt,
            n = 1, # number of images to return
            size = '1024x1024', # size of image
            )
    
    def set_image_url(self):
        self.image_url = self.image_response['data'][0]['url']
        
        
    def get_image_url(self):
        return self.image_url
    
    
    # Method to save image to local directory
    def save_image(self, filename):
        image_res = requests.get(self.image_url, stream=True)
        if image_res.status_code == 200:
            with open(filename, 'wb') as f:
                image_res.raw.decode_content = True
                shutil.copyfileobj(image_res.raw, f)
            del image_res
            return True
        else:
            print("Error loading image")
            return False
        
        