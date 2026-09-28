import streamlit as st
from src.auth import login_screen
from src.dashboard import render_dashboard

st.set_page_config(page_title="NEO TITANS | Mine Safety Rover", page_icon="🤖", layout="wide")

if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if not st.session_state.authenticated:
    login_screen()
else:
    render_dashboard()
