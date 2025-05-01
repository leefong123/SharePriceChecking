import json
import boto3
import os

def lambda_handler(event, context):
    # TODO implement
    message = event.get('message', 'No message provided')

    sns = boto3.client('sns')
    topic_arn = os.environ['SNS_TOPIC_ARN']

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
