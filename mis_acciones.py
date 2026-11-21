import yfinance as yf

print("=== Descargando datos de Apple ===")
data = yf.download("AAPL", period="5d")
print(data)
print("\n=== Último precio ===")
precio = data['Close'].iloc[-1].item()
print(f"${precio:.2f}")
