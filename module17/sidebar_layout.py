import streamlit as st

st.sidebar.header("sidebar")

st.sidebar.write("this is the sidebar")

st.sidebar.selectbox("choose an option",["Option 1","Option 2", "Option 3"])