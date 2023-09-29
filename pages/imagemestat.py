import streamlit as st

#image = './streramlit-io/static/cat_background.jpg'
image = "./streamlit-io/static/rainbow-lights-1491649.jpg"

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