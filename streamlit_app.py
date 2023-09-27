import streamlit
import pandas as pd

streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text("Omega 3 & Blueberry Oatmeal")
streamlit.text("Kale, Spinach, & Rocket Smoothie")
streamlit.text("Hard Boiled, Free-Range Eggs")



my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

streamlit.dataframe(my_fruit_list)

streamlit.header("Fruityvice Fruit Advice!")

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)


# gets json data
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
# displays it
streamlit.dataframe(fruityvice_normalized)
