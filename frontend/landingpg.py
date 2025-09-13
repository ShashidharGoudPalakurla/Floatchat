import streamlit as st
import requests




st.set_page_config(
    page_title="ARGO AI Ocean Explorer",
    
    layout="wide"
)


st.markdown(
    """
    <style>
    
   
   


    .stApp {
        background-image: url('https://i.pinimg.com/736x/86/f8/4b/86f84bf00e07cc71f76151118f764234.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
       
    }

    .hero-title{
        text-align:center;
        font-size:70px;
        margin-right:650px;
    }

    .title{
        text-align:center;
        font-size:100px;
        margin-right:450px;
        margin-top:0px;

    }

    .hero-sub{
        font-size:30px;
        margin-left: 220px;
    }

    .start-button{
        padding:10px 40px;
        border-radius: 50px;
        font-size:30px;
        margin-left:200px;
        margin-top: 100px;
        border:none;
        background-color:#001528;
    }

    </style>
    """,
    unsafe_allow_html=True
)


st.markdown('<div class="hero-title"> ARGO </div>', unsafe_allow_html=True)
st.markdown('<div class="title"> FloatChat</div>', unsafe_allow_html=True)

st.markdown('<div class="hero-sub"> tagline</div>', unsafe_allow_html=True)

st.markdown(
    """
    <a href="?page=front">
        <button class="start-button">
            Lets Dive!
        </button>
    </a>
    """,
    unsafe_allow_html=True
)











