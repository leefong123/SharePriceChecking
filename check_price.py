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
    else:
        report = "--"

    return report

report = check_stock()  
print(report)

if report != "--":
    exit(0)
    topic_arn = os.getenv("SNS_TOPIC_ARN")
    event = { "message" : report, "topic_arn" : topic_arn }
    lambda_client = boto3.client('lambda', region_name='ap-southeast-1')

    response = lambda_client.invoke(FunctionName='SendSNSEmail', InvocationType='Event', Payload=json.dumps(event))
    print("lambda client invocation response", response)
else:
    print("Not Match")
