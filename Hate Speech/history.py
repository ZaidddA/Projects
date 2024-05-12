import streamlit as st

def app():
    if 'history' not in st.session_state:
        st.session_state.history = []

    st.title("History")

    if st.session_state.history:
        st.write("Recent History:")
        for item in st.session_state.history:
            st.write(item)
    else:
        st.write("No history yet.")
