import boto3


def get_price(stock_code, threshold):
    ## point to note: to be replaced by actual code to retireve the  price here as to avoid chagrges to my personal aws account.
    ## run the check_price prgraom to test the share price retrieing portion
    price = 38   ## for testing only
    return price


def lambda_handler(event, context):

    stock_code = event.get('stock_code', 'No stock code')
    threshold = event.get('threshold', 'No threshold')

    ssm_client = boto3.client('ssm')
    response = ssm_client.get_parameter(Name='/SharePriceChecking/myapp/topic_arn')

    topic_arn = response['Parameter']['Value']

    price = get_price(stock_code, threshold)

    if (price < threshold):
        report = f"{stock_code} is below target ${threshold}, Price is ${price}\n"
        sns = boto3.client('sns')

        response  = sns.publish(
            TopicArn=topic_arn,
            Message=report,
            Subject="Lambda Email Notification"
        )
        print(f"Response ==> {response}")
        return {
            'statusCode': 200,
            'body': f"Message sent with ID: {response['MessageId']}"
        }
    else:
        return {
            'statusCode': 900,
            'body': "No action is required"
        }

