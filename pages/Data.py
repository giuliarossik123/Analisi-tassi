import streamlit as st
import pandas as pd 
import plotly.express as px
#import mymodel as m


st.set_page_config(page_title="Home", page_icon="static/favicon-32x32.png")
st.logo("static/uniupo-logo.svg", size="large")

st.title("Data")
name=st.sidebar.selectbox("Coin", options=["Bitcoin", "Dogecoin", "Ethereum"])
print(name)

df=pd.read_csv("static/data/df.csv")
st.dataframe(df)

plot=px.line(df, x="Datetime", y="Bitcoin", color_discrete_sequence=["#d92626"])
st.plotly_chart(plot)

c1,c2=st.columns(2)
c1.dataframe(df[["Datetime", name]])

plot =px.line(df, x="Datetime", y="Bitcoin", color_discrete_sequence=["#d92626"])
c2.plotly_chart(plot)