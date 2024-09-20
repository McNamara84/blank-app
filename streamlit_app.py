import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

file_path = 'data/BastarCraton.csv'
df = pd.read_csv(file_path)
cat_names = df.columns.to_list()[27:]

col1, col2 = st.columns(2)
with col1:
    choose_dataset = st.multiselect('Choose dataset', ['Bastor Craton'])
    el1 = st.selectbox('x axis', cat_names)
    el2 = st.selectbox('y axis', cat_names)
with col2:
    fig = plt.figure()
    plt.scatter(df[el1]/10000, df[el2]/10000)
    st.pyplot(fig)