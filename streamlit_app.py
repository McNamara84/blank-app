import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
file_path = 'data/BastarCraton.csv'
df = pd.read_csv(file_path)
st.dataframe(df)
st.title('Hello World!')
st.write('*Data Science Course*')
st.container(height=400, border=True).write(df)
