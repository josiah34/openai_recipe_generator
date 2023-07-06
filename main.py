import streamlit as st
from recipe import Recipe
from image import Image
def main():
    
    # Create recipe object
    recipe = Recipe()
    
    # Create AI Image object
    
    image = Image()
    
    st.title('👨‍🍳 OPENAI RECIPE GENERATOR 👩‍🍳')
    # Ingredients input 
    ingredients = st.text_input('Enter your ingredients separated by commas')

    # Button
    if st.button('Submit'):
        # Check if ingredients are entered
        if not ingredients or not ingredients.strip():
            st.warning("Please enter some ingredients")
        else:
            # Add ingredients to recipe object
            recipe.add_ingredient(ingredients)
            # Create recipe prompt from ingredients
            recipe.create_recipe_prompt()
            # Create recipe from the prompt using OpenAI API
            recipe.create_recipe()
            # Display recipe title
            st.write(recipe.get_recipe_title())
            # Create image prompt from recipe title
            image.create_image_prompt(recipe.get_recipe_title())
            # Create image from prompt using Dalle API
            image.create_image()
            image.set_image_url()
            
            # Display recipe
            st.write(recipe.response.choices[0].text)
            # Display image
            st.image(image.get_image_url(), caption=f"AI generated image of {recipe.get_recipe_title()}", use_column_width=True)
            
        
        
    




if __name__ == "__main__":
    main()
        