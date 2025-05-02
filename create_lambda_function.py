# Work in progress...
# automate creation and deletion of lambda  function and sns topic in separate program
# fire api call tfire api o perform real-time purchasing

import json
import boto3
import os


lambda_client = boto3.client('lambda', region_name='ap-southeast-1')
execute_role = os.getenv("LAMBDA_ROLE")

with open('function.zip', 'rb') as f:
    zipped_code = f.read()

response = lambda_client.create_function(
        FunctionName='SendSNSEmail',
        Runtime='python3.12',
        Role=execute_role,
        Handler='lambda_function.lambda_handler',
        Code=dict(ZipFile=zipped_code),
        Timeout=15
)

print("lambda client create function response", response)


