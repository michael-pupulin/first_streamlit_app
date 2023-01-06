import streamlit
import pandas

streamlit.title("My Parent's New Healthy Diner")

streamlit.subheader("Breakfast")
streamlit.text("Three egg omlet 7.99")
streamlit.text("Bacon sandwhich 8.99")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.text("Some of our avaialble fresh fruits")

selected = streamlit.multiselect("Go ahead and pick your favourites!:", list(my_fruit_list.Fruit))
to_show = my_fruit_list.loc[selected]

streamlit.dataframe(to_show)
