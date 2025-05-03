#### A program to scrape DBS share price from Yahoo Finance, check if the price falls below a target value, and if it does, send an email alert to the user
#### The alerting approach uses AWS Lambda to send an email via SNS   


##### Create an SNS topic for email notification. You can either use AWS management console or run create_sns_topic.py to create it 
$ python3 create_sns_function.py
  
![image](https://github.com/user-attachments/assets/57764dde-a2f3-49fb-bf04-bfe659a1060a)


##### Create a lambda function named SendSNSEmail by running the create_lambda_fucntion.py 

$ python3 create_lambda_function.py

![image](https://github.com/user-attachments/assets/50e395a2-ceaa-4115-adc8-97025a290c86)


##### Execute the code from the local host, it will invoke the Lambda function deployed on AWS, retrieve the share price, and publish it to SNS, which will then send an email to the user  

![image](https://github.com/user-attachments/assets/33b14c46-d742-462b-bdff-b34346e196fb)


##### An email notification containing the share price was received

![image](https://github.com/user-attachments/assets/e77724a4-4be7-47d3-b4ee-d1581dd1573e)


![image](https://github.com/user-attachments/assets/5d63b7d7-8b51-4743-995a-b9a7f24419e4)


##### Remove the lambda function by running the delete_lambda_function.py

![image](https://github.com/user-attachments/assets/5940c618-8799-4a2c-a992-bd2fb9b6e706)


##### Remove the SNS topic by running the delete_sns_topic.py

$ python3 delete_sns_topic.py

![image](https://github.com/user-attachments/assets/3b8bb6f4-174e-40f6-a265-3e2a8e0f762d)
