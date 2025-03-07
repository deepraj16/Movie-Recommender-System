import pickle
import streamlit as st
import requests

# Function to fetch movie poster using OMDb API
def fetch_poster(movie_name, api_key="b9686597"):
    url = f"http://www.omdbapi.com/?t={movie_name}&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    poster_url = data.get('Poster')

    if poster_url and poster_url != 'N/A':
        return poster_url
    else:
        return None  # No poster available

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    
    for i in distances[1:6]:
        # Get recommended movie name
        recommended_movie_name = movies.iloc[i[0]].title
        recommended_movie_names.append(recommended_movie_name)

        # Fetch the movie poster using OMDb API
        poster = fetch_poster(recommended_movie_name)
        recommended_movie_posters.append(poster)

    return recommended_movie_names, recommended_movie_posters


# Streamlit App Layout
st.header('Movie Recommender System')
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarty.pkl', 'rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display recommended movies and their posters
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3]) 
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4]) 