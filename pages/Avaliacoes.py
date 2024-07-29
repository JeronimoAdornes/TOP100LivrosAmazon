import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("asimov/datasets/customer reviews.csv")
df_top100_books = pd.read_csv("asimov/datasets/Top-100 Trending Books.csv")

books = df_top100_books["book title"].unique()
book = st.sidebar.selectbox("Books", books)

dfbook = df_top100_books[df_top100_books["book title"] == book]
df_reviews_f = df_reviews[df_reviews["book name"] == book]


book_title = dfbook["book title"].iloc[0]
book_genre = dfbook["genre"].iloc[0]
book_price = f"R${dfbook['book price'].iloc[0]}"
book_rating = dfbook["rating"].iloc[0]
book_year = dfbook["year of publication"].iloc[0]

st.title(book_title)
st.subheader(book_genre)
col1, col2, col3 = st.columns(3)
col1.metric("Preço", book_price)
col2.metric("Nota", book_rating)
col3.metric("Ano da Publicação", book_year)

st.divider()

for row in df_reviews_f.values:
    message = st.chat_message(f"{row[4]}")
    message.write(f"**{row[2]}**")
    message.write(row[5])

    # Estudar melhor este código para otimizar o mesmo
    # isso
