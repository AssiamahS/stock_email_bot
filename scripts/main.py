from fetch_stock.py import fetch_stock_data
from send_email.py import send_email

def main():
    stock_data = fetch_stock_data()
    stock_info = stock_data.to_string()
    send_email(stock_info)

if __name__ == "__main__":
    main()
