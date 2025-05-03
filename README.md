#### A program to scrape DBS share price from Yahoo Finance, check if the price falls below a target value, and if it does, send an email alert to the user
#### The alerting approach uses AWS Lambda to send an email via SNS   


##### Create an SNS topic for email notification. You can either use AWS management console or run create_sns_topic.py to create it 
$ python3 create_sns_function.py
  
![image](https://github.com/user-attachments/assets/57764dde-a2f3-49fb-bf04-bfe659a1060a)


##### Create a lambda function named SendSNSEmail by running the create_lambda_fucntion.py 

$ python3 create_lambda_function.py

![image](https://github.com/user-attachments/assets/50e395a2-ceaa-4115-adc8-97025a290c86)


##### Execute the code from the local host, it will retrieve the share price, invoke the AWS Lambda function deployed on AWS Cloud, and publish the share price to SNS which will then send an email to the user

![image](https://github.com/user-attachments/assets/e4454939-3193-4488-89da-817d41dc4641)


##### An email notification containing the share price was received

![image](https://github.com/user-attachments/assets/1d97c339-5699-4e89-801a-0a1bf7d89b72)


  

![image](https://github.com/user-attachments/assets/a77ae528-dfc5-463a-8f35-88ef2ae51dbf)


##### Remove the lambda function by running the delete_lambda_function.py

![image](https://github.com/user-attachments/assets/5940c618-8799-4a2c-a992-bd2fb9b6e706)


##### Remove the SNS topic by running the delete_sns_topic.py

$ python3 delete_sns_topic.py
