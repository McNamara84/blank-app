import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
file_path = 'data/BastarCraton.csv'
df = pd.read_csv(file_path)
#st.dataframe(df)
cat_names = df.columns.to_list()[27:]
st.title('Hello World!')
st.write('*Data Science Course*')
el1 = st.selectbox('Select element', cat_names)
#st.container(height=400, border=True)
