import streamlit as st
import numpy as np
import pandas as pd
import time

st.markdown("# Main page - Principal 🎈")
st.markdown("## Main page - Principal 🎈")
st.markdown("### Main page - Principal 🎈")
st.markdown("#### Main page - Principal 🎈")
st.markdown("##### Main page - Principal 🎈")
st.sidebar.markdown("# Main page - Side Bar 🎈")


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(dataframe.style.highlight_max(axis=0))

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

chart_data = pd.DataFrame(
     np.random.randn(20, 5),
     columns=['a', 'b', 'c', 'd', 'e'])

st.line_chart(chart_data)
st.table(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [-23.533773, -46.625290],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
y = st.slider('y')  # 👈 this is a widget
st.write(y, 'squared is', x * y)

st.text_input("Your name", key="val_qualquer")
st.write("""
         # My first app
         Aqui está o valor digitado:
         """)
# You can access the value at any point with:
st.session_state.val_qualquer

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data


df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option    

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


st.write('Starting a long computation...')
# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

st.write('...and now we\'re done!')