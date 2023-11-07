import streamlit as st

class NotFound:
    
    def __init__(self):
        self.title = 'NotFound'

    def view(self):
        st.title(self.title)
        st.write('Sorry, Not Found')