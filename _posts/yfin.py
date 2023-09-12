import yfinance as yf

ticker = input("Enter stock ticker: ")

# Download 3 months of historical data using the daily time frame
data = yf.download(ticker, period="3mo", interval="1d")
print(data)
