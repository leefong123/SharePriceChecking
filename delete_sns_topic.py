import boto3
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <parameter name>")
    sys.exit(1)

para_name = sys.argv[1]

ssm_client = boto3.client('ssm')
response = ssm_client.get_parameter(Name=para_name)
topic_arn = response['Parameter']['Value']

sns_client = boto3.client('sns')
response = sns_client.delete_topic(TopicArn=topic_arn)
print("SNS topic deleted:", response)


response = ssm_client.delete_parameter(Name=para_name)
print("Parameter store deleted:", response)

