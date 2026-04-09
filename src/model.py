from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(df):
    df = df.dropna()

    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)

    features = ['RSI', 'MACD', 'MACD_signal']
    X = df[features]
    y = df['Target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    print("Model Accuracy:", model.score(X_test, y_test))

    return model