import streamlit as st
from iris_dataset.iris import iris

if "sidebar_state" not in st.session_state :
    st.session_state.sidebar_state = "expanded"

st.set_page_config(
    page_title="EDA Portfolio",
    layout="wide",
    initial_sidebar_state=st.session_state.sidebar_state
    )

def collapse_sidebar() :
    st.session_state.sidebar_state = "collapsed" if st.session_state.sidebar_state == "epxanded" else "collapsed"

iris_button = st.sidebar.button("Iris Dataset")

if iris_button :
    collapse_sidebar()
    iris("iris_dataset/results")    
