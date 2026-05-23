import pandas as pd
import streamlit as st
import plotly.express as px

from module14.Lineplot import avg_iq_by_continent
from module3.sets import unique_array

#df = pd.DataFrame({
 #   'Name': ['Arianita','Festa','Gresa'],
#  'Age': [23,23,21],
#    'City':['Prishtin','Prizren','Vushtrri']
#})

#df

books_df = pd.read_csv('eda-amazon-top-50-bestselling-books.ipynb')

st.title("bestselling books in amazon ")
st.write("this app analyzes the amazon top sellig books")

st.subheader("summary statistics")
total_books = books_df.shape[0]
unique_titles = books_df['name']
avg_rating = books_df['user rating']
avg_price = books_df['price']

col1, col2, col3, col4 = st.columns(4)
col1.metric("total_books", total_book   s)