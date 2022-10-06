import streamlit as st
import streamlit.components.v1 as components
def app():
    st.title('Chest X-ray')
    #st.write("check out this [link](https://chest-xray-api.herokuapp.com/)")
    components.iframe("https://chest-xray-api.herokuapp.com/",width=1050, height=1760, scrolling=True)
