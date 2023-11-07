import streamlit as st

class Home:
        
    def __init__(self):
        self.title = 'Home'

    def view(self):
        st.title(self.title)
        st.write('Hello World!')