import streamlit as st
def show_chatbot_ui():
   st.markdown("""
    <style>
 
    .stApp {
        background:;
        color: white;
        font-family: 'Poppins', sans-serif;
        padding:100px;
         
        
    }

 
    .stChatMessage.user {
        background-color: #0f3460;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 8px 0;
        color: #ffffff;
        font-weight: 500;
        max-width: 500px; 
        width:100%; 
    }

  
    .stChatMessage.assistant {
        background-color: #e94560;
        border-radius: 15px;
        padding: 10px 15px;
        margin: 8px 0;
        color: white;
        font-weight: 500;
        max-width: 500px;
        width:100%;  
    }

    .stChatInput:focus-within {
     border: 2px solid deepskyblue;   
     box-shadow: 0 0 6px deepskyblue; 
     border-radius:18px;
    }
               
    [data-testid="stChatInput"] {
    width: 100% !important;            
    max-width: 700px;                 
    margin: 0 auto;                   
}

[data-testid="stChatInput"] textarea {
    width: 100% !important;           
    resize: none !important;           
    box-sizing: border-box
}

   
    
    </style>
               
     """, unsafe_allow_html=True)


   st.set_page_config(page_title="FloatChat", page_icon="💬", layout="centered")
   
   st.title("FloatChat")
   
   
   if "messages" not in st.session_state:
       st.session_state.messages = []
   
   
   for msg in st.session_state.messages:
       if msg["role"] == "user":
           st.chat_message("user", avatar="./pngwing.com.png").markdown(msg["content"])
       else:
           st.chat_message("assistant").markdown(msg["content"])
   
   
   if prompt := st.chat_input("Need help?... I'm here!"):
       
       st.session_state.messages.append({"role": "user", "content": prompt})
       st.chat_message("user", avatar="./pngwing.com.png").markdown(prompt)
   
   
       response = f"Echo: {prompt}"
       
    
    
       st.session_state.messages.append({"role": "assistant", "content": response})
       st.chat_message("assistant").markdown(response)
   