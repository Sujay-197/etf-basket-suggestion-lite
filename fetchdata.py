import yfinance as yf
import os

def fetch_historical_data(symbol, period="ytd"):
    ticker = yf.Ticker(symbol)
    data = ticker.history(period=period)
    os.makedirs("stocks_csv", exist_ok=True)
    csv_filename = f"stocks_csv/{symbol}data.csv"
    data.to_csv(csv_filename)
    print(f"Data saved to {csv_filename}")
    return data[["Open", "Close", "High", "Low", "Volume"]]


result = fetch_historical_data("AAPL")
print(result)



