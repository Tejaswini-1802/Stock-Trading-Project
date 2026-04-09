def generate_signals(df):
    df['Buy']=(df['RSI'] < 30) & (df['MACD'] > df['MACD_Signal'])
    df['Sell']=(df['RSI'] > 70) & (df['MACD'] < df['MACD_Signal'])
    return df