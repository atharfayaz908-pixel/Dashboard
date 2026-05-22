import streamlit as st
impor pandas as pd 
import numpy as np

#page configuration
st.set_page_config(page_title = "dashboard",
                   page_icon ="Screenshot 2026-04-06 155002.png",
                   layout = "wide"
                   initial_sidebar_state ="expanded"
                   )

st.title("student performance Dashboard")
st.write("This is the sample dashboard")



data = {
    "T1":[66,89,78,92],
    "T2": [91,68,68,82],
    "T3":[76,99,68,72],
}

df= pd.Dataframe(data,index=["s1","s2","s3","s4"])

st.subheader("Marks card")
st.dataframe(df)


st.sunheader("performance")
st.line_chart(df.T)
