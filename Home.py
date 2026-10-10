import streamlit as st

st.set_page_config(page_title="Home", page_icon=":house:")

st.title("World Cities")
st.write("Welcome to the World Cities app!")
st.write("This is the home page. Click the button below to open the main application.")

if st.button("Go to App"):
    try:
        st.switch_page("pages/app.py")
    except AttributeError:
        st.warning("Please open the 'App' page from the sidebar or make sure app.py is inside the pages folder.")
