import streamlit as st
from streamlit_lottie import st_lottie
import requests


def load_lottieurl(url: str):       
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Ocean animation
lottie_ocean = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_t24tpvcu.json")


st.set_page_config(
    page_title="ARGO AI Ocean Explorer",
    
    layout="wide"
)


st.markdown(
    """
    <style>
    
    /* Remove Streamlit container background for Lottie */
    div[data-testid="stAnimation"] > div {
        background: none !important;       /* remove background */
        padding: 0 !important;            /* remove padding */
        margin: 0 auto !important;        /* center horizontally */
        box-shadow: none !important;      /* remove shadow */
        border: none !important;          /* remove border */
    }
      div[data-testid="stAnimation"] > div {
        background: transparent !important;
        padding: 0 !important;
        box-shadow: none !important;
        border: none !important;
    }
   
   


    .stApp {
        background-image: url('https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
       
    }

    /* Hero Section */
    .hero-title {
        font-size: 60px;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(45deg, #00eaff, #0077ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 10px;
    }
    .hero-sub {
        text-align: center;
        font-size: 22px;
        font-weight: 500;
        color: #f8f8f8;
        text-shadow: 1px 1px 6px #000000;
        margin-bottom: 40px;
    }

    /* Feature cards */
.feature-card {
    background: linear-gradient(135deg, rgba(0,60,80,0.85), rgba(0,40,70,0.85));
    padding: 22px;
    border-radius: 14px;
    margin: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.45);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.feature-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 28px rgba(0,0,0,0.6);
}

/* CTA Section */
.cta {
    text-align: center;
    margin-top: 20px;
    background: linear-gradient(90deg, #c77dff, #ff4da6, #00eaff);
    padding: 25px 0;
    border-radius: 20px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.5);
}
.cta p {
    font-size:22px;
    font-weight:100;
    color: #ffffff;  /* White text on gradient */
    text-shadow:1px 1px 6px rgba(0,0,0,0.5);
}
.cta-btn {
    background: #ffffff;
    color: #00eaff;
    font-size: 20px;
    font-weight: bold;
    padding: 14px 32px;
    border-radius: 40px;
    border: none;
    cursor: pointer;
    box-shadow: 0 6px 18px rgba(0,0,0,0.4);
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}
.cta-btn:hover {
    transform: scale(1.08);
    box-shadow: 0 8px 22px rgba(0,0,0,0.6);
}

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="hero-title"> ARGO AI Ocean Explorer</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Where Data Meets the Deep — Time, Depth & Intelligence in One Place.</div>', unsafe_allow_html=True)


st.write("---")


col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div class="feature-card">
            <h3> Deep Time–Depth Analytics</h3>
            <p class="tagline">“Unveil the hidden stories beneath every ocean layer.”</p>
            <p>Generate <b>heatmaps & vertical profiles</b> for temperature, salinity, and BGC parameters. Unlock deep climate insights across time and depth.</p>
        </div>
        <div class="feature-card">
            <h3> 3D Trajectory Mapping</h3>
            <p class="tagline">“Follow ARGO floats across space and depth — like never before.”</p>
            <p>Explore ARGO floats in <b>interactive 3D</b> (Longitude–Latitude–Depth). Rotate, zoom, and reveal the hidden currents of our oceans.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        """
        <div class="feature-card">
            <h3> Conversational Ocean AI</h3>
            <p class="tagline">“Ask the ocean in plain words, get science-backed insights.”</p>
            <p>Ask queries like <i>“Show salinity near the equator”</i>. Our <b>RAG-powered AI</b> translates questions into precise data queries.</p>
        </div>
        <div class="feature-card">
            <h3> Smart Dashboards & Insights</h3>
            <p class="tagline">“Visualize. Compare. Export. All in one intuitive dashboard.”</p>
            <p>Use <b>geospatial maps, interactive plots, and parameter comparisons</b>. Export results in NetCDF, CSV, or ASCII formats.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# Optional Future Section
st.markdown(
    """
    <div class="feature-card" style="text-align:center;">
        <h3> Future Horizons</h3>
        <p class="tagline">“Expanding to gliders, buoys, and satellite data for a unified ocean view.”</p>
        <p>Our vision extends beyond ARGO floats — integrating <b>gliders, buoys, and satellite datasets</b> to create the most comprehensive ocean intelligence platform.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("---")


st.markdown(
    """
    <div class="cta">
        <p style="font-size:22px; font-weight:400; color:white; text-shadow:1px 1px 6px #00000091;">
          Ready to explore the deep blue with AI-powered insights?</p>
        <button class="cta-btn" onclick="window.location.href='pages/explorer.py'"> Launch  Explorer</button>
    </div>
    """,
    unsafe_allow_html=True
)
