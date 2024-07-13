import streamlit as st
import pickle
import requests

# movies_list=movies_list['title'].values  # movie_list =[avatar,pitates of something' ....]
# print(movies_list)


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


st.title("Select Movie to recommend")

# Fetching pickle file
movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]

    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]
    print(movies_list)
    recommended_movies=[]
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies,recommended_movie_posters


option = st.selectbox('Select Movies', (movies['title'].values))

if st.button("Recommend"):
    recommended_movies,recommend_movie_posters=recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommend_movie_posters[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommend_movie_posters[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommend_movie_posters[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommend_movie_posters[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommend_movie_posters[4])