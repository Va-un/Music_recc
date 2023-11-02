import streamlit as st
import pandas as pd

df = pd.read_csv("Recc.csv",index_col = "Unnamed: 0")

def similar(target_word):
    # Find similar words within the DataFrame
    similar_words = df[df['song_title'].str.contains(target_word, case=False, na=False)]
    return similar_words.song_title.values


def predictor(name,inp ,link = df):
    getting_closer_id = link[link['song_title'] == name]['clusters']
    val = getting_closer_id.values[0]
    result = link[link['clusters'] == val]['song_title'].head(inp)
    return result

st.image('good_times_with_bad_music_1050x700.jpg')




try:
    st.text('Enter Song name')
except:
    # Handle the exception and display a warning message
    st.warning("No Song Found")


val = st.text_input("Name")
song = st.selectbox("Pick one", similar(val))
inp = st.slider('No of Recommender Song', 0, 40, 5)


if st.button('Similar Songs'):
    value = predictor(song,inp)
    st.dataframe(value)
    st.button("Reset", type="primary")
else:
    st.write('')

# Define the link text and URL
slink_text = "Spotify"
slink_url = "https://open.spotify.com"

# Create a hyperlink
st.markdown(f"[{slink_text}]({slink_url})")

ylink_text = "Youtube Music"
ylink_url = "https://music.youtube.com"

# Create a hyperlink
st.markdown(f"[{ylink_text}]({ylink_url})")