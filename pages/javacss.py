import streamlit as st

st.button('Click me!')

css='''
<style>
    .stButton > button {
        color: red;
    }
    .stButton > button:hover {
        color: violet;
        border-color: violet;
    }
    .stButton > button:focus {
        color: purple !important;
        border-color: purple !important;
        box-shadow: purple 0 0 0 .2rem;
    }
</style>
'''

st.markdown(css, unsafe_allow_html=True)