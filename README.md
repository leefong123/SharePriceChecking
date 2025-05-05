#### A project to scrape DBS share price from Yahoo Finance, check if the price falls below a target value, and if it does, send an email alert to the user.The alerting approach uses AWS Lambda to send an email via SNS   



##### Follow the following step-by-step guide to create and manage AWS resources
Summary of Steps to create and manage AWS Resources
1.	Create an SNS topic and store its ARN in Parameter Store
2.	Create Lambda function on AWS
3.	Invoke the AWS Lambda function
4.	Delete the Lambda function from AWS
5.	Delete the SNS topic, its subscription and the related Parameter Store

  


1.To create an SNS topic and store its ARN in Parameter Store, run the following command
   
$ python3 create_sns_topic.py SNSByEmail abc123@gmail.com  

The SNS topic named SNSByEmail was created, and is currently pending for subscription confirmation. To complete the subscription process, go to your email account and click on the subscription link.

![image](https://github.com/user-attachments/assets/3cf0eedf-2675-48fe-ac74-9a69efdd1076)

 
Once the subscription’s status changed to “Confirmed”, you should be able to receive emails from SNS.  


![image](https://github.com/user-attachments/assets/04a69129-6bb8-4810-a327-09d279d6539c)

 

2. To create the Lambda function on AWS, run the following command, providing the function name you want to use and the execution role that the Lambda function will assume. Make sure the role is created in AWS and has the permission to publish to SNS and retrieve parameters from Parameter Store.

$ python3 create_lambda_function.py <lambda function name> <execution role>  


Lambda function was created   

 ![image](https://github.com/user-attachments/assets/84cbcbec-40ff-4129-b6d1-ce53d93fb399)

 
3. To test if the Lambda function is working, run the following command. It invokes the Lambda function stored in the AWS, which retrieves the share price and publishes the information to SNS which in turn sends an email notification to subscribed user.   

$ python3 invoke_lambda_function <lambda function name>  


The email was received successfully  

 ![image](https://github.com/user-attachments/assets/6b1c093f-e7c4-4be1-9e31-3ac9f9c7607d)


4. To delete the Lambda function stored on AWS, run the following command
$ python3 delete_lambda_function <lambda function name>

No Lambda function was found   


![image](https://github.com/user-attachments/assets/4d4400c9-2dd0-4cda-bc28-407ce8fdb202)


5. To delete the SNS topic, its subscription and the related Parameter Store, run the following command.

$ python3 python3 delete_sns_topic.py <parameter name>  


No SNS Topic was found  


 ![image](https://github.com/user-attachments/assets/5d06d1f4-8129-46de-9974-f0d95d7df6a3)





