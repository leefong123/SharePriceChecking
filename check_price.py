import json
import os
import requests
import schedule
import time
import smtplib
from email.mime.text import MIMEText
import yfinance as yf
from datetime import datetime
import boto3

def check_stock():
    print("Retrieving data...")
    threshold = 48
    ticker = yf.Ticker("D05.SI")
    price = ticker.info.get('regularMarketPrice')
    currency = ticker.info.get('currency')
    name = ticker.info.get('longName')
    report = ""


    if price < threshold:
        report = f"{name} is below target ${threshold}, Price is ${price}\n"

    if report:
       now = datetime.now()
       timestamp = now.strftime("%Y%m%d %H%M%S")
       log_message = f"{timestamp} {report}"
       print(log_message)
       with open("/tmp/check-price.log", "a") as f:
            f.write(log_message)
       #send_email(report)
    else:
        print("Do nothing")

    return report


def send_email(message):
    sender = os.getenv("MAIL_SENDER")
    recipient = os.getenv("MAIL_USER")
    subject = os.getenv("MAIL_SUBJECT")
    appkey = os.getenv("MAIL_APPKEY")
    
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(recipient, appkey)
    server.sendmail(sender, [recipient], msg.as_string())
    server.quit()
    print("Email sent!")

schedule.every().day.at("18:00").do(check_stock)    ## execute daily at 6 pm
#schedule.every(10).seconds.do(check_stock)   # for testing only
report = check_stock()   # for testing only
print(report)

lambda_client = boto3.client('lambda', region_name='ap-southeast-1')
event = { "message" : report }
response = lambda_client.invoke(FunctionName='SendSNSEmail', InvocationType='Event', Payload=json.dumps(event))
print("lambda client invocation response", response)


#print("Scheduler started...")
#while True:
#    schedule.run_pending()
#    time.sleep(1)

