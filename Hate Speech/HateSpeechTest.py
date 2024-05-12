import streamlit as st
from streamlit_option_menu import option_menu
import home, trending, account, your, about, history, posts

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Aspect-Based Hate Speech Detection App",
        page_icon="🚀",
        layout="centered",
    )

    st.title("Aspect-Based Hate Speech Detection App")

    with st.sidebar:
        app = option_menu(
            menu_title='Aspect-Based Hate Speech Detection App ',
            options=['Home', 'Account', 'Trending', 'Your Posts', 'History', 'Posts', 'About'],
            icons=['house-fill', 'person-circle', 'trophy-fill', 'chat-fill', 'clock-history', 'file-earmark-post-fill', 'info-circle-fill'],
            menu_icon='chat-text-fill',
            default_index=1,
            styles={
                "container": {"padding": "5!important", "background-color": 'black'},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                             "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"}, }
        )

    if app == "Home":
        home.app()
    elif app == "Account":
        account.app()
    elif app == "Trending":
        trending.app()
    elif app == 'Your Posts':
        your.app()
    elif app == 'History':
        history.app()
    elif app == 'Posts':
        posts.app()
    elif app == 'About':
        about.app()

if __name__ == "__main__":
    main()
