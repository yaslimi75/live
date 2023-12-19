#!/usr/bin/env python
# coding: utf-8

# In[1]:
import streamlit as st
import pandas as pd
import plotly.express as px

# Set the title of the app
st.title('Airbnb Paris Analyse de marché V2')
st.title('Hello)

# URL to fetch the data
DATA_URL = ('http://data.insideairbnb.com/france/ile-de-france/paris/2023-09-04/visualisations/listings.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Load and cache the data
data_load_state = st.text('Chargement des données...')
data = load_data(10000)
data_load_state.text("Fait! (using st.cache)")

# Display raw data if checkbox is checked
if st.checkbox('Afficher les données raw'):
    st.subheader('Raw data')
    st.write(data)

# Average Price in Paris
st.subheader('Prix Moyen à Paris')
average_price_paris = data['price'].mean()
st.write(f"Le prix moyen à Paris est de {average_price_paris:.2f} €")

# Average Price per Neighborhood (Interactive)
st.subheader('Prix Moyen par Quartier (Interactif)')
average_price_per_neighborhood = data.groupby('neighbourhood')['price'].mean().reset_index()
fig = px.bar(average_price_per_neighborhood, x='neighbourhood', y='price', 
             labels={'price': 'Prix Moyen', 'neighbourhood': 'Quartier'},
             title="Prix Moyen par Quartier à Paris")
st.plotly_chart(fig)

# Number of Properties per Neighborhood
st.subheader('Nombre de Biens par Quartier')
count_per_neighbourhood = data['neighbourhood'].value_counts()
st.bar_chart(count_per_neighbourhood)

# Dynamic Map with Housing Prices
st.subheader('Carte Dynamique avec Prix des Logements')
# Ensure your data has 'latitude' and 'longitude' columns for this to work
st.map(data)

# Bar Plot of Number of Properties per Owner
st.subheader('Nombre de Logements par Propriétaire')
properties_per_owner = data['host_name'].value_counts().head(10)  # Top 10 owners
st.bar_chart(properties_per_owner)

# Note: This code assumes that your dataset has the columns 'price', 'neighbourhood', 'latitude', 'longitude', and '


