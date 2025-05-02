import boto3

lambda_client = boto3.client('lambda', region_name='ap-southeast-1')

response = lambda_client.delete_function(
    FunctionName='SendSNSEmail'
)

print("Lambda function deleted.", response)

