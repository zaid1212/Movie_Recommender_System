import streamlit as st
import pickle
import pandas as pd

with open('movies1.pkl', 'rb') as file:
    movies_list = pickle.load(file)
st.title("Movie Recommender System")

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies_list[movies_list['title']==movie].index[0]
    distance = similarity[movie_index]
    rec_movies = sorted(list(enumerate(distance)), reverse=True,key=lambda x: x[1])[1:6]

    recomended_movies = []
    for i in rec_movies:
        recomended_movies.append(movies_list.iloc[i[0]].title)
    return recomended_movies


selected_movie_name = st.selectbox('How would you like to be contacted?',movies_list['title'].values)
if st.button('Recommend'):
    recomendations = recommend(selected_movie_name)
    for i in recomendations:
        st.write(i)
