
import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣omega 3 and Blueberry Oatmeal')
streamlit.text('🥗kale,Spinach & rocket smoothi')
streamlit.text('🍗Hard-Boiled Free Range Egg')
streamlit.text('🥑🍞avocado Toast')

streamlit.header('🍌🥭Build Your Own Fruit Smoothi🥝🍇 ')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
