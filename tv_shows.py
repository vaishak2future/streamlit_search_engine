import streamlit as st
import pandas as pd
from fuzzywuzzy import process

#Read the CSV into Pandas Dataset
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

#Return top elements in list that match the query
def match(query,title_list):
    return [ i[0] for i in process.extract(query,title_list)]

#Return all elements with higher ages than query age + all
def age_filter(query_age,age_list):
    age_list = [int(str(i).replace('+','')) for i in age_list]
    return list(set([ str(i)+"+" for i in age_list if i<=int(query_age)])) + ['all']
    

# Load Data Frame
tv_shows = load_data('tv_shows.csv')
tv_shows.reset_index(drop=True, inplace=True)

# Copy of Data Frame for Age Filtering
age_df = tv_shows[tv_shows['Age'].notna()]
age_df = age_df[age_df['Age']!="all"]

# Short-hand variables
title = tv_shows['Title']
age = age_df['Age']

# Render Title
st.write("TV Show Search Engine")

# String Search
string_input = st.text_input("Search below", "Enter Show Name Here")
st.write(tv_shows[title.isin(match(string_input,title))][["Title","Age","IMDb","Netflix","Hulu","Prime Video","Disney+"]])

# Age Filter
age_input = st.text_input("Filter by Age", "10")
st.write(tv_shows[tv_shows['Age'].isin(age_filter(age_input,age))][["Title","Age"]])