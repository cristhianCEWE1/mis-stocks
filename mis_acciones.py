import yfinance as yf

tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]

print("=== Precios actuales ===")
for ticker in tickers:
    data = yf.download(ticker, period="5d")
    precio = data['Close'].iloc[-1].item()
    cambio = ((data['Close'].iloc[-1] - data['Close'].iloc[0]) / data['Close'].iloc[0] * 100).item()
    print(f"{ticker}: ${precio:.2f}  ({cambio:+.2f}%)")

print("\n=== Análisis de Apple (3 meses) ===")
aapl = yf.download("AAPL", period="3mo")
aapl['SMA_20'] = aapl['Close'].rolling(window=20).mean()
aapl['SMA_50'] = aapl['Close'].rolling(window=50).mean()

delta = aapl['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
aapl['RSI'] = 100 - (100 / (1 + rs))

print(aapl[['Close', 'SMA_20', 'SMA_50', 'RSI']].tail())
print(f"\nRSI actual: {aapl['RSI'].iloc[-1].item():.2f}")
