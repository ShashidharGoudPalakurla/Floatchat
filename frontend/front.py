import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import sqlite3
from datetime import datetime, timedelta
from timedepthplot import show_time_depth_plot
from map_page import show_map
from chatbot_ui import show_chatbot_ui
st.set_page_config(
    page_title="ARGO-FloatChat",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
        margin: 40px;
        
    }
    
    .stApp {
        
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
        background-image: url("https://images.unsplash.com/photo-1604599340287-2042e85a3802?q=80&w=774&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
    }
    
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 40px;
        margin-top: 90px;
        backdrop-filter: blur(10px);
        font-size:70px;
        margin-bottom: 20px;
    }
    
    .logo {
        color: white;
        font-size: 24px;
        font-weight: bold;
        letter-spacing: 2px;
    }
    
    .nav-links {
        display: flex;
        gap: 10px;
        align-items: centre;
        font-size:px;
    }
    
    div.stButton > button:first-child {
        background: none;
        color: white;
        border-radius: 0px;
        height: 50px;
        width: 200px;
        font-size: 1000px;
        font-weight: bold;
        border:0px solid #2E8B57;
        transition: 0.3s;
    }

    .main-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-height: 70vh;
        color: white;
        padding: 0 20px;
    }
    
   
     .earth-title {
        font-size: 80px;
        font-weight: 300;
        letter-spacing: 8px;
        margin-bottom:0px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    
    .description {
        max-width: 600px;
        font-size: 16px;
        line-height: 1.6;
        margin-top: 100px;
        opacity: 0.9;
    }
    
    
    
    
    
    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            gap: 10px;
            padding: ;
            font-size:70px;
        }
        
        .earth-title {
            font-size: 50px;
            letter-spacing: 4px;
        }
        
        .description {
            font-size: 14px;
        }
    }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def create_dummy_data():
    
    conn = sqlite3.connect("dummy.db", check_same_thread=False)
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time TIMESTAMP,
        depth REAL,
        latitude REAL,
        longitude REAL,
        salinity REAL,
        temperature REAL,
        air_temp REAL,
        oxygen REAL
    )
    """)
    
    cursor.execute("SELECT COUNT(*) FROM profiles")
    if cursor.fetchone()[0] == 0:
        np.random.seed(42)
        base_time = datetime(2024, 1, 1, 0, 0, 0)
        lat, lon = 12.9716, 77.5946 
        
        rows = []
        for i in range(100):  
            t = base_time + timedelta(days=i*3)
            depth = np.random.choice([0, 10, 20, 50, 100, 200]) 
            latitude = lat + np.random.randn() * 0.1
            longitude = lon + np.random.randn() * 0.1
            salinity = 34 + np.random.rand() * 2  
            temperature = 15 + np.random.rand() * 10  
            air_temp = 20 + np.random.rand() * 5   
            oxygen = 200 + np.random.rand() * 50  
            rows.append((t, depth, latitude, longitude, salinity, temperature, air_temp, oxygen))
        
        base_time_2025 = datetime(2025, 1, 1, 0, 0, 0)
        for i in range(100):  
            t = base_time_2025 + timedelta(days=i*3)
            depth = np.random.choice([0, 10, 20, 50, 100, 200]) 
            latitude = lat + np.random.randn() * 0.1
            longitude = lon + np.random.randn() * 0.1
            salinity = 34.5 + np.random.rand() * 2  # Slightly different for comparison
            temperature = 16 + np.random.rand() * 10  
            air_temp = 21 + np.random.rand() * 5   
            oxygen = 210 + np.random.rand() * 50  
            rows.append((t, depth, latitude, longitude, salinity, temperature, air_temp, oxygen))
        
        cursor.executemany("""
        INSERT INTO profiles (time, depth, latitude, longitude, salinity, temperature, air_temp, oxygen)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, rows)
        
        conn.commit()
    
    return conn

@st.cache_data
def load_data():
    conn = create_dummy_data()
    df = pd.read_sql_query("SELECT * FROM profiles", conn)
    df['time'] = pd.to_datetime(df['time'])
    df['year'] = df['time'].dt.year
    return df

def navigate_to(page):
    st.session_state.current_page = page
    st.rerun()


col2, col3, col4, col5, col6 = st.columns([ 2, 2, 2, 2, 2])

with col2:
    if st.button(" Home", use_container_width=True):
        navigate_to('home')

with col3:
    if st.button(" FloatChat", use_container_width=True):
        navigate_to('chatbot')

with col4:
    if st.button(" Map Trajectory", use_container_width=True):
        navigate_to('map')

with col5:
    if st.button(" Profile Comparison", use_container_width=True):
        navigate_to('comparison')

with col6:
    if st.button(" Depth-Time Plot", use_container_width=True):
        navigate_to('time_depth')



if st.session_state.current_page == 'home':
    st.markdown("""
    <div class="main-content">
        <div class="earth-title">ARGO</div>
        <div class="earth-title">FloatChat</div>
        <div class="description">
            Learn more about this fascinating miracle that we call our home, Planet Earth. 
            Explore ARGO float data, analyze ocean profiles, and discover the secrets of our oceans.
        </div>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.current_page == 'chatbot':
   

   
    
    show_chatbot_ui()
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'map':
    st.markdown('<div class="page-content">', unsafe_allow_html=True)

    st.title("Map Trajectory")
    st.write("Visualize the trajectory of ARGO floats across the ocean.")

    show_map()   # renamed function

    st.markdown('</div>', unsafe_allow_html=True)


elif st.session_state.current_page == 'comparison':
 
    st.title(" Profile Comparison")
    
    
    df = load_data()
    
    main_col, sidebar_col = st.columns([0.7, 0.3])
    
    with sidebar_col:
        st.markdown('<div class="comparison-sidebar">', unsafe_allow_html=True)
        st.subheader("Controls")
        
        available_years = sorted(df['year'].unique())
        
        st.write("**Select Time range to Compare:**")
        year1 = st.selectbox("From", available_years, index=0, key="year1_select")
        year2 = st.selectbox("To", available_years, index=1 if len(available_years) > 1 else 0, key="year2_select")
        
        properties = ['salinity', 'temperature', 'air_temp', 'oxygen']
        selected_property = st.selectbox("Choose Profile", properties, key="property_select")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with main_col:
        df_year1 = df[df['year'] == year1]
        df_year2 = df[df['year'] == year2]
        
        st.subheader(f"{selected_property.title()} Comparison: {year1} vs {year2}")
        
        df_year1_plot = df_year1.copy()
        df_year1_plot['year_label'] = f'{year1}'
        df_year2_plot = df_year2.copy()
        df_year2_plot['year_label'] = f'{year2}'
        
        combined_df = pd.concat([df_year1_plot, df_year2_plot])
        
        fig_combined = px.line(combined_df, 
                              x='time', 
                              y=selected_property,
                              color='year_label',
                              title=f"{selected_property.title()} Time Series Comparison",
                              color_discrete_map={f'{year1}': 'blue', f'{year2}': 'red'})
        
        st.plotly_chart(fig_combined, use_container_width=True)
        
        st.subheader("Distribution Comparison")
        fig_box = go.Figure()
        
        fig_box.add_trace(go.Box(y=df_year1[selected_property], 
                                name=f'{year1}', 
                                boxpoints='outliers',
                                marker_color='blue'))
        
        fig_box.add_trace(go.Box(y=df_year2[selected_property], 
                                name=f'{year2}', 
                                boxpoints='outliers',
                                marker_color='red'))
        
        fig_box.update_layout(title=f"{selected_property.title()} Distribution Comparison",
                             yaxis_title=selected_property.title())
        
        st.plotly_chart(fig_box, use_container_width=True)
        
        st.subheader("Individual Analysis")
        year_col1, year_col2 = st.columns(2)
        
        with year_col1:
            fig1 = px.line(df_year1, 
                          x='time', 
                          y=selected_property,
                          title=f"{selected_property.title()} - {year1}",
                          color_discrete_sequence=['blue'])
            st.plotly_chart(fig1, use_container_width=True)
        
        with year_col2:
            fig2 = px.line(df_year2, 
                          x='time', 
                          y=selected_property,
                          title=f"{selected_property.title()} - {year2}",
                          color_discrete_sequence=['red'])
            st.plotly_chart(fig2, use_container_width=True)
        
        st.subheader("Statistical Summary")
        
        stats_col1, stats_col2 = st.columns(2)
        
        with stats_col1:
            st.write(f"**{year1} Statistics:**")
            st.write(f"Mean: {df_year1[selected_property].mean():.2f}")
            st.write(f"Standard deviation: {df_year1[selected_property].std():.2f}")
            st.write(f"Min: {df_year1[selected_property].min():.2f}")
            st.write(f"Max: {df_year1[selected_property].max():.2f}")
        
        with stats_col2:
            st.write(f"**{year2} Statistics:**")
            st.write(f"Mean: {df_year2[selected_property].mean():.2f}")
            st.write(f"Standard deviation: {df_year2[selected_property].std():.2f}")
            st.write(f"Min: {df_year2[selected_property].min():.2f}")
            st.write(f"Max: {df_year2[selected_property].max():.2f}")
    
    st.markdown('</div>', unsafe_allow_html=True)

elif st.session_state.current_page == 'time_depth':
    st.markdown('<div class="page-content">', unsafe_allow_html=True)
    show_time_depth_plot()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)