import json
import boto3
import os

topic_arn = os.getenv("SNS_TOPIC_ARN")

event = { "stock_code": "D05.SI", "topic_arn" : topic_arn, "threshold" : 50}
lambda_client = boto3.client('lambda', region_name='ap-southeast-1')
response = lambda_client.invoke(FunctionName='SendSNSEmail', InvocationType='Event', Payload=json.dumps(event))
print("lambda client invocation response", response)

