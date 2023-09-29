import streamlit as st

#image = './app/static/cat_background.jpg'
image = "./app/static/rainbow-lights-1491649.jpg"

css = f'''
<style>
    .stApp {{
        background-image: url({image});
    }}
    .stApp > header {{
        background-color: transparent;
    }}
</style>
'''
st.markdown(css, unsafe_allow_html=True)