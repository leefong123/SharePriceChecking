import boto3


ssm_client = boto3.client('ssm')
response = ssm_client.get_parameter(Name='/SharePriceChecking/myapp/topic_arn')
topic_arn = response['Parameter']['Value']

sns_client = boto3.client('sns')
response = sns_client.delete_topic(TopicArn=topic_arn)
print("SNS topic deleted:", response)


response = ssm_client.delete_parameter(Name='/SharePriceChecking/myapp/topic_arn')
print("Parameter store deleted:", response)

