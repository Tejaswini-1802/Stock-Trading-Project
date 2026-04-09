from data_loader import load_data
from features import add_indicators
from strategy import generate_signals
from model import train_model

df = load_data()
df = add_indicators(df)
df = generate_signals(df)

model = train_model(df)

df.to_csv("outputs/final_data.csv", index=False)