import streamlit as st
import pandas as pd

df = pd.read_csv("../outputs/final_data.csv")

st.title("📈 Reliance Stock Analysis")

st.line_chart(df['Close'])

st.write("Buy Signals", df[df['Buy'] == True].tail())
st.write("Sell Signals", df[df['Sell'] == True].tail())