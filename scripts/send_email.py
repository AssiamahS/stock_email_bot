import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

def send_email(stock_info):
    with open('data/config.json', 'r') as file:
        config = json.load(file)
    
    sender = config['email']['sender']
    receiver = config['email']['receiver']
    password = config['email']['password']
    smtp_server = config['email']['smtp_server']
    smtp_port = config['email']['smtp_port']

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = "Daily Stock Update"
    
    body = f"Here is your stock update for today:\n\n{stock_info}"
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

# Example usage
if __name__ == "__main__":
    stock_info = "AAPL: $150.00"
    send_email(stock_info)
