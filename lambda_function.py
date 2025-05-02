import json
import boto3
import os

def lambda_handler(event, context):
    message = event.get('message', 'No message provided')

    topic_arn = event.get('topic_arn', 'No topic arn')

    sns = boto3.client('sns')

    response  = sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject="Lambda Email Notification"
    ) 
    return {
        'statusCode': 200,
        'body': f"Message sent with ID: {response['MessageId']}"
        #'body': json.dumps('Hello from Lambda!')
    }
