import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide", 
    page_title="MA payroll data"
)

st.title('MA State Payroll')
st.write('Only showing results > $100M. Data courtesy of cthrupayroll.mass.gov')

df = pd.read_csv("data/Entire_Payroll_20241123.csv")

df_trimmed = df[~(df['Total'] <= 100000000)]  

data = pd.DataFrame(df_trimmed, columns=["Departments", "Total"])
sorted_data = data.sort_values('Total')

st.bar_chart(sorted_data, x="Departments", y="Total", use_container_width=True, height=700)
