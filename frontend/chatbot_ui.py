import streamlit as st


st.set_page_config(page_title="FloatChat", page_icon="💬", layout="centered")

st.title("FloatChat")


if "messages" not in st.session_state:
    st.session_state.messages = []


for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])


if prompt := st.chat_input("Need help?... I'm here!"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user", avatar="./pngwing.com.png").markdown(prompt)


    response = f"Echo: {prompt}"
    
 
 
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)
