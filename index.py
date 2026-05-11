import streamlit as st
import random 

#sidebar
st.sidebar.title("Menu")

pagina = st.sidebar.selectbox(
    "Escolha uma página",
    ["Home", "Grafíco"]
)
#Home 
if pagina == "Home":
    
    st.title ("Página Home")
    
    st.write("Sistema usando o Streamlit")
    
    #input
    nome=st.text_input("Digite seu nome")

#selectbox    