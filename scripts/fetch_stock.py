import yfinance as yf
import json

def fetch_stock_data():
    with open('data/config.json', 'r') as file:
        config = json.load(file)
    
    ticker = config['stock']['ticker']
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    
    return data

# Example usage
if __name__ == "__main__":
    stock_data = fetch_stock_data()
    print(stock_data)
