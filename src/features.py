import pandas as pd
from ta.momentum import RSIIndicator
from ta.trend import MACD
def add_features(df):
    df['RSI']=RSIIndicator(df['Close']).rsi()
    macd=MACD(df['Close'])
    df['MACD']=macd.macd()
    df['MACD_Signal']=macd.macd_signal()
    return df