# openai_recipe_generator

I made this project in order to gain a better understanding of the OPENAI API and its available models. In this project I created a recipe generator using the `text-davinci-003` and `DALLE-E`. I used the streamlit library in order to create my frontend. 

The app works by asking the user to enter ingredients that they have then building a prompt which request a recipe based on the ingredients that the user entered. The created prompt is fed into the completion api call. After that the response is used to display the returned recipe. We also extract the recipe title in order to create an ai generated image using DALL-E. The response from DALL-E gives us a url which is used to display the image along with the created recipe. 

Bon appetit !! 


**Models:**
- text-davinci-0003
- DALLE-E


**Libraries:**
- streamlit 
- openai 
- os
- python-dotenv
- requests 
- shutil 
- re (regular expression)



**Usage:**

Install requirements:

``pip install -r requirements.txt``


Set your OPENAI API KEY 

RUN APP:

``streamlit run main.py ``




![recipe-generator](https://github.com/josiah34/openai_recipe_generator/assets/25124463/e328a020-a2de-49a2-bef4-f9731daeeacc)




