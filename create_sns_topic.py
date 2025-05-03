import boto3
import os


sns_topic = os.getenv("SNS_TOPIC")
user_email = os.getenv("MAIL_USER")


sns = boto3.client('sns')
response = sns.create_topic(Name=sns_topic)
print(f"Topic ARN: {response['TopicArn']}")


topic_arn =  response['TopicArn']

response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=user_email
)

print(f"Subscription ARN (pending confirmation): {response['SubscriptionArn']}")



