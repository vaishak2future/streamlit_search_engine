import streamlit as st
import pandas as pd
from fuzzywuzzy import process

#Read the CSV into Pandas Dataset
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

#Return top elements in list that match the query
def match(query,list):
    results = []
    return [ i[0] for i in process.extract(query,list)]
    

st.write("TV Show Search Engine")
user_input = st.text_input("Search below", "Enter Show Name Here")
tv_shows = load_data('tv_shows.csv')
tv_shows.reset_index(drop=True, inplace=True)
title = tv_shows['Title']
st.write(tv_shows[title.isin(match(user_input,title))])