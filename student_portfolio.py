import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.header('The Best Company')

content = '''While the definition of a "best" company may vary, certain characteristics are 
universally recognized as hallmarks of success. Innovation, employee well-being, social responsibility, 
customer focus, adaptability, and effective leadership collectively contribute to the distinction of the 
best companies in various industries. As businesses continue to evolve, aspiring to embody these traits can 
pave the way for long-term success and positive societal impact.'''

content = content.title()

st.write(content)

st.title("Our Team")

col1, col2, col3 = st.columns([1, 1, 1])

#name department photo

df = pd.read_csv("data.csv", sep=",")

with col1:
    for index, row in df[:4].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images 2/"+row['image'])


with col2:
    for index, row in df[4:8].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images 2/" + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        st.header(f"{row['first name'].title()} {row['last name'].title()}")
        st.write(row['role'])
        st.image("images 2/" + row['image'])


