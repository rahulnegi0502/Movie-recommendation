import pandas as pd
import streamlit as st
import pickle
import requests
def fetch_poster(movie_id):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=ee394f26a2c44e1b9822d347de511653&language=en-US'.format(movie_id))
    data=response.json()
    return "https://image.tmdb.org/t/p/original/"+data['poster_path']



movie_list=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))
movies=pd.DataFrame(movie_list)
def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommend_movies=[]
    recommend_posters=[]
    for i in movies_list:
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return recommend_movies,recommend_posters

st.title('Movie Recommender System')
movie_name=st.selectbox('Movie Name',movies['title'].values)
if st.button('Recommend'):
    m,p=recommend(movie_name)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(m[0])
        st.image(p[0])
    with col2:
        st.text(m[1])
        st.image(p[1])
    with col3:
        st.text(m[2])
        st.image(p[2])
    with col4:
        st.text(m[3])
        st.image(p[3])
    with col5:
        st.text(m[4])
        st.image(p[4])







