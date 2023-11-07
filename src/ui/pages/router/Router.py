import streamlit as st
from ui.pages.Home import Home
from ui.pages.NotFound import NotFound
from ui.pages.DataLake import DataLake

class Router:
    
    @staticmethod
    def init_page():
        if 'disp_page' not in st.session_state:
            st.session_state.disp_page: str = 'Home'


    @staticmethod
    def get_pages():
        return [
            'Home',
            'DataLake',
            ]



    @staticmethod
    def view():
        '''disp_pageに設定されているページを表示する'''
        
        if st.session_state.disp_page == 'Home':
            print('Render Home')
            Home().view()
        
        elif st.session_state.disp_page == 'DataLake':
            print('Render DataLake')
            DataLake().view()
            
        else:
            NotFound().view()
            
            
