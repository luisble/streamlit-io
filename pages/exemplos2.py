import streamlit as st
# import numpy as np
# import pandas as pd
# import time

col1, col2 = st.columns(2)

original = Image.open(image)
col1.header("Original")
col1.image(original, use_column_width=True)

grayscale = original.convert('LA')
col2.header("Grayscale")
col2.image(grayscale, use_column_width=True)

st.title("Let's create a table!")
for i in range(1, 10):
    cols = st.columns(4)
    cols[0].write(f'{i}')
    cols[1].write(f'{i * i}')
    cols[2].write(f'{i * i * i}')
    cols[3].write('x' * i)

# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

# Space out the maps so the first one is 2x the size of the other three
c1, c2, c3, c4 = st.columns((2, 1, 1, 1))

my_expander = st.expander()
my_expander.write('Hello there!')
clicked = my_expander.button('Click me!')
