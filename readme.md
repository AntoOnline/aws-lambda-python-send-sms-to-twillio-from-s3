This Lambda function is triggered by an S3 bucket event, and then sends the SMS to Twilio.

## Process ##
1. Trigger this Lambda function by an S3 bucket event for an object PUT event.  
2. The function will read the SMS named like this: +274012312344, then read the body. 
3. The content is then sent to the Twilio API.
4. The object (+274012312344) is then deleted from the S3 bucket. 

For delivery statuses etc:
Get the delivery report from the Twilio Console or API. 
For the API: 
https://api.twilio.com/2010-04-01/Accounts/<TWILIO_ACCOUNT_SID>/Messages.csv?PageSize=1000. 
Set auth to 'Basic Auth'. Set the username to TWILIO_ACCOUNT_SID. Set the password to TWILIO_AUTH_TOKEN.

## Setup Lambda function ##
1. Log in to the AWS Console.
2. Open the 'Lambda Functions' service.
3. Click on the 'create function' button.
4. Click the 'author from scratch' option.
5. Enter a Lambda function name.
6. Set the runtime to 'Python 3.8'
7. Change the default execution role to: 'Create a new role with basic Lambda permissions'.
8. Click the 'create function' button.
9. The function should now be created. Next, click on the 'upload from' button in the code tab, choose zip, and then upload the provided code.
10. Click on the 'configuration' tab and then the 'environment variables' option.
11. Add FROM_NUMBER and specify the 'from' number at Twilio.
12. Add TWILIO_ACCOUNT_SID	and specify your Twilio account ID.
13. Add TWILIO_AUTH_TOKEN	and specify your Twilio auth token.
14. Click on the configuration tab and click the 'permissions' option.
15. Click on the role name in the execution role section.
16. Click 'add inline policy'.
17. Choose the 'S3' service.
18. Choose ‘ListBucket’, ‘DeleteObject’, ‘GetObject’. 
19. Click on the 'review policy' button.
20. Choose a specific or all resource. A specific resource is better.
21. Give the policy a name.
22. Click on the 'create policy' button.

## Setup the S3 Bucket ##
1. Open the 'S3' service.
2. Click the 'create bucket' button.
3. Enter a bucket name.
4. Click the 'create bucket' button.

## Assign the Lambda Trigger Event ##
2. Open the S3 bucket service.
3. Click the 'properties' tab.
4. Click on the 'create event notification' button.
5. Enter an event name.
6. Select the 'put' event type.
7. Choose the 'Lambda function' destination.
8. Choose the Lambda function you have created.
