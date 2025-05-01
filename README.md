### 
#### v0.1 23402025 A simple program to scrape DBS share price from Yahoo Finance, check if the price falls below a target value, and if it does, send an email alert to the user.
#### v0.2 01052025 Integrated with AWS lambda to send SNS email  




  
##### Create an SNS topic for email notifications

![image](https://github.com/user-attachments/assets/57764dde-a2f3-49fb-bf04-bfe659a1060a)

##### Execute the code from the local host to retrieve the share price and invoke the AWS Lambda function

![image](https://github.com/user-attachments/assets/e4454939-3193-4488-89da-817d41dc4641)


##### The email notification is sent by SNS, which is triggered by a Lambda function
![image](https://github.com/user-attachments/assets/73625ab8-0253-42a5-ba90-185052572381)


##### An email containing the share price was received
![image](https://github.com/user-attachments/assets/dd607439-d9cf-4074-8f66-43b9716c6bba)


