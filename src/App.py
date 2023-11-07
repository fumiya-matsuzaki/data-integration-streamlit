import streamlit as st
from ui.pages.router.Router import Router

class App:
    # stateの初期化
    Router.init_page()
    
    # 認証やページごとに表示する選択肢を変えるためにstreamlitのマルチページ機能は使わないようにしている
    pages = Router.get_pages()
        
    st.session_state.disp_page = st.sidebar.selectbox(
            label='Page',
            options=pages
        )
    
    Router.view()
    