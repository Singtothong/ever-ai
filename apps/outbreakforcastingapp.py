import streamlit as st
import streamlit.components.v1 as components
def app():
    #st.title('Outbreak Forecasting')
    st.write("check out this [link](http://ever-forecasting.herokuapp.com)")
    components.iframe("http://ever-forecasting.herokuapp.com",width=1050, height=1760, scrolling=True)
