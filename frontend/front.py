import streamlit as st
import pandas as pn
import numpy as np
import json
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="ARGO - Planet Earth",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Remove padding from main container */
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    
    /* Full height background */
    .stApp {
        background-image: url('https://argo.ucsd.edu/wp-content/uploads/sites/361/2020/10/Thomas-JessinLOV-768x563.png');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        min-height: 100vh;
    }
    
    /* Navigation bar styling */
    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 40px;
        background: rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    .logo {
        color: white;
        font-size: 24px;
        font-weight: bold;
        letter-spacing: 2px;
    }
    
    .nav-links {
        display: flex;
        gap: 30px;
        align-items: center;
    }
    
    .nav-link {
        color: white;
        text-decoration: none;
        font-size: 16px;
        font-weight: 500;
        padding: 8px 16px;
        border-radius: 20px;
        transition: all 0.3s ease;
    }
    
    .nav-link:hover {
        background: rgba(255, 255, 255, 0.1);
        color: #64B5F6;
    }
    
    .enroll-btn {
        background: white;
        color: #1a1a2e;
        padding: 10px 24px;
        border-radius: 25px;
        font-weight: bold;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .enroll-btn:hover {
        background: #f0f0f0;
        transform: translateY(-2px);
    }
    
    /* Main content styling */
    .main-content {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-height: 80vh;
        color: white;
        padding: 0 20px;
    }
    
    .planet-title {
        font-size: 16px;
        font-weight: 300;
        letter-spacing: 4px;
        margin-bottom: 20px;
        opacity: 0.8;
    }
    
    .earth-title {
        font-size: 80px;
        font-weight: 300;
        letter-spacing: 8px;
        margin-bottom: 40px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    
    .description {
        max-width: 600px;
        font-size: 16px;
        line-height: 1.6;
        margin-bottom: 40px;
        opacity: 0.9;
    }
    
    .get-started-btn {
        background: rgba(255, 255, 255, 0.9);
        color: #1a1a2e;
        padding: 15px 40px;
        border-radius: 30px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        cursor: pointer;
        transition: all 0.3s ease;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .get-started-btn:hover {
        background: white;
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
    }
    
    /* Responsive design */
    @media (max-width: 768px) {
        .navbar {
            flex-direction: column;
            gap: 20px;
            padding: 20px;
        }
        
        .nav-links {
            flex-wrap: wrap;
            justify-content: center;
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

# Navigation bar
st.markdown("""
<div class="navbar">
    <div class="logo">ARGO</div>
    <div class="nav-links">
        <a href="#" class="nav-link">ARGO Float Profile</a>
        <a href="#" class="nav-link">Map Trajectory</a>
        <a href="#" class="nav-link">Profile Comparisons</a>
        <a href="#" class="nav-link">Time Depth Plots</a>
        <button class="enroll-btn">Enroll</button>
    </div>
</div>
""", unsafe_allow_html=True)

# Main content
st.markdown("""
<div class="main-content">
    <div class="planet-title">PLANET</div>
    <div class="earth-title">EARTH</div>
    <div class="description">
        Learn more about this fascinating miracle that we call our home, Planet Earth. Course enrollment 
        starts today. Early Bird tickets typically last a week, don't miss out!
    </div>
    <button class="get-started-btn">GET STARTED</button>
</div>
""", unsafe_allow_html=True)

# Add some spacing at the bottom
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)