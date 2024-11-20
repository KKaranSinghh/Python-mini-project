# Terminal -> cd Dashboard -> Enter
# streamlit run Home.py -> Enter

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as ps
import plotly.graph_objects as go

st.sidebar.image('Assets\Black Gold Elegant Simple Real Estate Logo (1) (1).jpg')
st.sidebar.header('Company stablished on 7 Nov 2024, Mr. KARAN SINGH is the Founder of the Company.')
st.sidebar.header('Gmail :- ks780374@gmail.com')
st.sidebar.header('Phone no. :- 835489****')

st.markdown("<h1 style='color: black; font-weight: bold; background-color: lightpink; border: 2px solid black; text-align: center; padding: 10px;'>Real Estate Dataset Analysis</h1>",unsafe_allow_html=True)
st.image('banner.png', use_column_width= True)
st.markdown('# **Description**')
st.markdown('This dataset contains various features of residential properties along with their corresponding prices. It is suitable for exploring and analyzing factors influencing housing prices and for building predictive models to estimate the price of a property based on its attributes.')
st.markdown('# **Analysation & Visualization of:**')
st.markdown('* Distribution of Furnishing status between houses')
st.markdown('* Price distribution by number of bedrooms')
st.markdown('* Relationship between area and house price')
st.markdown('* Average house price based on main road access')
st.markdown('* Average house price by hot water heating and air conditioning')
st.markdown('* Number of rooms and average price of house')
st.markdown('* Correlation matrix heatmap')
st.markdown('* Average price by furnishing status')
st.markdown('* Relation between mainroad, parking and basement')
st.markdown('* house price distribution by basement availability')
