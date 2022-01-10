import streamlit as st

st.title('Hello Wilders, welcome to my application!')
st.write("I enjoy to discover streamlit possibilities")

name = st.text_input("Please give me your name :")
name_length = len(name)
st.write("Your name has ",name_length,"characters")

# Lien pour les données weather

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/weather2019.csv"

import pandas as pd
df_weather = pd.read_csv(link)
st.write(df_weather)

# Exemple avec la 'magic command' c'est à dire que streamlit sait parfois quoi afficher sans avoir à écrire st.write :
# df_weather

# Graphique automatique avec streamlit
st.title('Graphique avec streamlit')
st.line_chart(df_weather['MAX_TEMPERATURE_C'])

# Graphique avec seaborn
st.title('Graphique avec seaborn')
import seaborn as sns
viz_correlation = sns.heatmap(df_weather.corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

# Graphique avec plotly
# st.title('Graphique avec plotly')
# import plotly.express as px

# fig = px.scatter(df_weather, x='DAY', y='PRECIP_TOTAL_DAY_MM', color='OPINION', animation_frame ='MONTH', size='CLOUDCOVER_AVG_PERCENT') #Complete this code
# fig.update_yaxes(range=[-10,40])
# st.plotly_chart(fig)
