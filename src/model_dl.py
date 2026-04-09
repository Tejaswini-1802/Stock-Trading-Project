import yfinance as yf
import pandas as pd
def load_data():
    df=yf.download("RELIANCE.NS",start="2010-01-01",end="2025-01-01"),
    df.reset_index(inplace=True)
    return df

if __name__=="__main__":
    df=load_data()
    df.to_csv("data/stock.csv",index=False)
    print("Data Saved Successfully")
    