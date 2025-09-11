import streamlit as st 
import pandas as pd
import numpy as np
import sqlite3
import matplotlib.pyplot as plt 
import plotly.express as px 




conn= sqlite3.connect("dummy.db")
df=pd.read_sql("SELECT *FROM profiles", conn)
conn.close()

df['time'] = pd.to_datetime(df['time'])

st.set_page_config(
   page_title="Depth-Time Plot",
   page_icon= "🌊",
   layout="wide",
   initial_sidebar_state="expanded",
)
st.title("Depth-Time Plot")

parameter = st.sidebar.selectbox(
    "Select Parameter",
    ["temperature", "salinity", "air_temp", "oxygen"]
)
if isinstance(df['depth'].iloc[0], bytes):
    df['depth'] = df['depth'].apply(lambda x: int.from_bytes(x, byteorder='little'))

min_depth, max_depth = st.sidebar.slider(
    "Select Depth Range (m)",
    int (df['depth'].min()),
    int(df['depth'].max()),
    (int(df['depth'].min()), int(df['depth'].max()))
)



filtered_df = df[(df['depth'] >= min_depth) & (df['depth'] <= max_depth)]

heatmap_data = filtered_df.pivot(index='depth', columns='time', values=parameter)

fig = px.imshow(
    heatmap_data.sort_index(ascending=False),
    labels=dict(x="Time", y="Depth(m)", color=parameter.capitalize()),
    aspect="auto",
    color_continuous_scale= 'Rainbow'

)
st.plotly_chart(fig, use_container_width=True)

