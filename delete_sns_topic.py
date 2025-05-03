import boto3
import os


topic_arn = os.getenv("SNS_TOPIC_ARN")
sns_client = boto3.client('sns')
response = sns_client.delete_topic(TopicArn=topic_arn)
print("SNS topic deleted:", response)

