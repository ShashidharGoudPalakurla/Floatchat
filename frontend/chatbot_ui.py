import streamlit as st
import requests
import time
import json
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def query_backend(user_query):
    """Query the backend API at http://127.0.0.1:5000/query"""
    try:
        response = requests.post(
            "http://127.0.0.1:5000/query", 
            json={"query": user_query},
            headers={"Content-Type": "application/json"},
            timeout=30
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            st.error(f"Backend error: {response.status_code}")
            return None
            
    except requests.exceptions.ConnectionError:
        # Fallback demo data 
        time.sleep(2)
        return [{
            "depth_levels": [
                {"pres": 3.4, "salinity": 36.327, "temp": 26.355},
                {"pres": 5.1, "salinity": 36.326, "temp": 26.356},
                {"pres": 7.1, "salinity": 36.326, "temp": 26.357},
                {"pres": 9.3, "salinity": 36.325, "temp": 26.356},
                {"pres": 11.2, "salinity": 36.325, "temp": 26.355},
                {"pres": 13.3, "salinity": 36.324, "temp": 26.355},
                {"pres": 15.4, "salinity": 36.325, "temp": 26.354},
                {"pres": 17.4, "salinity": 36.322, "temp": 26.344},
                {"pres": 19.5, "salinity": 36.324, "temp": 26.332},
                {"pres": 21.3, "salinity": 36.316, "temp": 26.329},
                {"pres": 23.3, "salinity": 36.308, "temp": 26.300},
                {"pres": 25.3, "salinity": 36.283, "temp": 26.100},
                {"pres": 27.1, "salinity": 36.252, "temp": 25.719},
                {"pres": 29.2, "salinity": 36.215, "temp": 25.200},
                {"pres": 31.4, "salinity": 36.154, "temp": 23.792}
            ],
            "lat": 22.851356666666668,
            "lon": 60.49283333333333,
            "profile_id": 65,
            "query_explain": f"Based on your query about '{user_query}', I found oceanographic data from the Indian Ocean. The surface temperature is around 26.3°C, but it gets cooler as you go deeper. Think of it like this: warm at the top, gradually getting cooler down below. 🌊🌡️ The salinity (saltiness) is also fairly consistent in the upper layers.",
            "time": "2025-09-01 02:57:20"
        }]
        
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return None

def create_ocean_data_charts(depth_data):
    """Create beautiful charts for ocean data visualization"""
    if not depth_data:
        return None
    
    pressures = [d["pres"] for d in depth_data]
    temperatures = [d["temp"] for d in depth_data]
    salinities = [d["salinity"] for d in depth_data]
    
    fig = make_subplots(
        rows=1, cols=2,
        subplot_titles=('Temperature vs Depth', 'Salinity vs Depth'),
        specs=[[{"secondary_y": False}, {"secondary_y": False}]]
    )
    
    fig.add_trace(
        go.Scatter(
            x=temperatures,
            y=pressures,
            mode='lines+markers',
            name='Temperature',
            line=dict(color='#ff6b6b', width=3),
            marker=dict(size=6, color='#ff6b6b'),
            hovertemplate='<b>Temperature</b><br>Temp: %{x:.2f}°C<br>Depth: %{y:.1f} dbar<extra></extra>'
        ),
        row=1, col=1
    )
    
    fig.add_trace(
        go.Scatter(
            x=salinities,
            y=pressures,
            mode='lines+markers',
            name='Salinity',
            line=dict(color='#4ecdc4', width=3),
            marker=dict(size=6, color='#4ecdc4'),
            hovertemplate='<b>Salinity</b><br>Salinity: %{x:.3f} PSU<br>Depth: %{y:.1f} dbar<extra></extra>'
        ),
        row=1, col=2
    )
    
    
    fig.update_layout(
        title=dict(
            text='Ocean Data Profile',
            font=dict(size=20, color='white'),
            x=0.5
        ),
        showlegend=False,
        height=400,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white')
    )
    
    fig.update_xaxes(
        title_text="Temperature (°C)",
        gridcolor='rgba(255,255,255,0.1)',
        row=1, col=1
    )
    fig.update_xaxes(
        title_text="Salinity (PSU)",
        gridcolor='rgba(255,255,255,0.1)',
        row=1, col=2
    )
    fig.update_yaxes(
        title_text="Pressure (dbar)",
        autorange="reversed",  
        gridcolor='rgba(255,255,255,0.1)',
        row=1, col=1
    )
    fig.update_yaxes(
        title_text="Pressure (dbar)",
        autorange="reversed",
        gridcolor='rgba(255,255,255,0.1)',
        row=1, col=2
    )
    
    return fig

def show_thinking_animation():
    """Display thinking animation"""
    thinking_placeholder = st.empty()
    
    for i in range(12):
        dots = "." * ((i % 3) + 1)
        thinking_placeholder.markdown(
            f"""
            <div class="thinking-container">
                <div class="thinking-text">🌊 Anton is analyzing ocean data{dots}</div>
            </div>
            """, 
            unsafe_allow_html=True
        )
        time.sleep(0.25)
    
    return thinking_placeholder

def display_metadata(data):
    """Display metadata in a clean format"""
    metadata_html = f"""
    <div class="metadata-container">
        <div class="metadata-item">📍 <strong>Location:</strong> {data.get('lat', 'N/A'):.3f}°N, {data.get('lon', 'N/A'):.3f}°E</div>
        <div class="metadata-item">🕒 <strong>Time:</strong> {data.get('time', 'N/A')}</div>
        <div class="metadata-item">🆔 <strong>Profile:</strong> {data.get('profile_id', 'N/A')}</div>
    </div>
    """
    st.markdown(metadata_html, unsafe_allow_html=True)

def show_chatbot_ui():
    st.set_page_config(
        page_title="FloatChat", 
        layout="wide",
        page_icon="🌊"
    )

    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        font-family: 'Inter', sans-serif;
        color: white;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display: none;}
    
    /* Header */
    .main-header {
        text-align: center;
        padding: 2rem 0;
        margin-bottom: 2rem;
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(45deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        font-size: 1.2rem;
        color: rgba(255, 255, 255, 0.8);
        font-weight: 400;
    }
    
    /* Chat Container */
    .chat-container {
        max-width: 900px;
        margin: 0 auto;
        padding: 0 1rem;
    }
    
    /* Chat Messages - Fixed Alignment */
    .stChatMessage {
        margin: 1.5rem 0 !important;
        padding: 0 !important;
    }
    
    /* User Message - Right Aligned */
    .stChatMessage[data-testid="chat-message-user"] {
        display: flex !important;
        justify-content: flex-end !important;
        align-items: flex-start !important;
    }
    
    .stChatMessage[data-testid="chat-message-user"] > div {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        padding: 1rem 1.5rem !important;
        border-radius: 20px 20px 5px 20px !important;
        max-width: 70% !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3) !important;
        margin-left: auto !important;
    }
    
    /* Assistant Message - Left Aligned */
    .stChatMessage[data-testid="chat-message-assistant"] {
        display: flex !important;
        justify-content: flex-start !important;
        align-items: flex-start !important;
    }
    
    .stChatMessage[data-testid="chat-message-assistant"] > div {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        padding: 1rem 1.5rem !important;
        border-radius: 20px 20px 20px 5px !important;
        max-width: 80% !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
        margin-right: auto !important;
    }
    
    /* Thinking Animation */
    .thinking-container {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        padding: 1rem 1.5rem !important;
        border-radius: 20px 20px 20px 5px !important;
        max-width: 80% !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2) !important;
        margin-right: auto !important;
    }
    
    .thinking-text {
        color: rgba(255, 255, 255, 0.8);
        font-style: italic;
    }
    
    /* Chat Input */
    .stChatInput > div {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 25px !important;
        max-width: 900px !important;
        margin: 0 auto !important;
    }
    
    .stChatInput textarea {
        background: transparent !important;
        color: white !important;
        border: none !important;
        font-family: 'Inter', sans-serif !important;
        padding: 1rem 1.5rem !important;
    }
    
    .stChatInput textarea::placeholder {
        color: rgba(255, 255, 255, 0.6) !important;
    }
    
    .stChatInput button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        border: none !important;
        border-radius: 50% !important;
        color: white !important;
        width: 40px !important;
        height: 40px !important;
        margin: 0.5rem !important;
    }
    
    /* Metadata */
    .metadata-container {
        margin-top: 1rem;
        padding: 1rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 10px;
        border-left: 3px solid #667eea;
    }
    
    .metadata-item {
        display: inline-block;
        margin: 0.25rem 1rem 0.25rem 0;
        font-size: 0.9rem;
        color: rgba(255, 255, 255, 0.8);
    }
    
    /* Hide chat avatars */
    .stChatMessage img {
        display: none !important;
    }
    
    /* Responsive */
    @media (max-width: 768px) {
        .main-title {
            font-size: 2rem;
        }
        
        .stChatMessage[data-testid="chat-message-user"] > div,
        .stChatMessage[data-testid="chat-message-assistant"] > div {
            max-width: 90% !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Header
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">🌊 FloatChat-Anton</h1>
        <p class="subtitle">AI-powered ocean data analysis with beautiful visualizations</p>
    </div>
    """, unsafe_allow_html=True)

    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat container
    with st.container():
        # Display chat history
        for msg in st.session_state.messages:
            if msg["role"] == "user":
                with st.chat_message("user"):
                    st.markdown(msg["content"])
            else:
                with st.chat_message("assistant"):
                    # Display the AI response text
                    st.markdown(msg["content"])
                    
                    # Display metadata if it exists
                    if "metadata" in msg:
                        display_metadata(msg["metadata"])
                    
                    # Display chart if it exists
                    if "chart_data" in msg:
                        chart = create_ocean_data_charts(msg["chart_data"])
                        if chart:
                            st.plotly_chart(chart, use_container_width=True, config={'displayModeBar': False})

    
    if user_input := st.chat_input("Ask me about ocean data..."):

        # Add user message to session state
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            # Show thinking animation
            thinking_placeholder = show_thinking_animation()
            
            # Query backend
            response_data = query_backend(user_input)
            thinking_placeholder.empty()

            if response_data and len(response_data) > 0:
                data = response_data[0]  # Get first item from array
                
                if "query_explain" in data:
                    # Display AI response
                    ai_response = data["query_explain"]
                    st.markdown(ai_response)
                    
                    # Display metadata
                    display_metadata(data)
                    
                    # Create message object for session state
                    message_obj = {
                        "role": "assistant", 
                        "content": ai_response,
                        "metadata": data  # Store metadata separately
                    }
                    
                    # Create and display charts
                    if "depth_levels" in data and data["depth_levels"]:
                        chart = create_ocean_data_charts(data["depth_levels"])
                        if chart:
                            st.plotly_chart(chart, use_container_width=True, config={'displayModeBar': False})
                            # Store chart data instead of the chart object
                            message_obj["chart_data"] = data["depth_levels"]
                    
                    # Add to session state
                    st.session_state.messages.append(message_obj)
                else:
                    error_msg = "No explanation available in the response."
                    st.markdown(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})
            else:
                error_msg = "🚫 Sorry, I couldn't retrieve ocean data right now. Please try again!"
                st.markdown(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

if __name__ == "__main__":
    show_chatbot_ui()