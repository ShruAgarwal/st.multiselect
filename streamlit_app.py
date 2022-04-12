import streamlit as st
import pandas as pd

st.title('**st.multiselect**')
st.write('*Displays a multiselect widget*')

# Desert collection
df = pd.DataFrame({
     'deserts': ['Cupcakes 🧁', 'Cheesecake 🍰', ' Apple pie 🥧', 'Pancakes 🥞', 'Hot chocolate 🍫', 'Doughnuts 🍩', 'Ice cream 🍨', 'Custard pudding 🍮']
     })

options = st.multiselect(
     'Pick your favorite deserts',
     df['deserts'])

st.write('You selected:', options)
