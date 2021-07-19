# Description: 
# Trigger this Lambda function by an S3 bucket event for an object PUT event.  
# The function will read the SMS named like this: +274012312344, then read the 
# body. The content is then sent to the Twilio API. The object (+274012312344) 
# is then deleted from the S3 bucket. You can then get the delivery report 
# from the Twilio Console or API. 
# 
# For the API: 
# https://api.twilio.com/2010-04-01/Accounts/<TWILIO_ACCOUNT_SID>/Messages.csv?PageSize=1000. 
# Set auth to 'Basic Auth'. Set the username to TWILIO_ACCOUNT_SID. 
# Set the password to TWILIO_AUTH_TOKEN.

import os
import sys
import json
import boto3
import traceback
import urllib.parse
from pprint import pprint
from twilio.rest import Client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    print('Start')

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the Lambda environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    from_number = os.environ['FROM_NUMBER']

    # Read the SMS info from the bucket
    # Object name must be a valid phone like: +27403517742
    print('Get bucket and object name')
    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        to_number = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    except:
        traceback.print_exc(file=sys.stdout)
        return {
            "state": "error",
            "error": "Could not read the bucket name or object key. This function must be triggered by an S3 Put event."
        }

    # Read the mesage body from the object
    print('Get object body')
    try:    
        response = s3.get_object(Bucket=bucket, Key=to_number)
        body = response['Body'].read().decode()

        print('To : '+to_number)
        print('Body : '+body)
    except:
        deleteSMS(bucket,to_number)
        traceback.print_exc(file=sys.stdout)
        return {
            "state": "error",
            "error": "Could not read object body."
        }

    # Send the message to Twillio
    print('Send SMS to Twillio')
    try:
        client = Client(account_sid, auth_token)

        message = client.messages \
                    .create(
                        body=body,
                        from_=from_number,
                        to=to_number
                    )

        print('Twillio Message ID: ' + message.sid)
    except:
        deleteSMS(bucket,to_number)
        traceback.print_exc(file=sys.stdout)
        return {
            "state": "error",
            "error": "Could not read object body."
        }

    print('Delete message from bucket')        
    deleteSMS(bucket,to_number)

    print('Done')
    return {
        "state": "success",
        "messageSID": message.sid
    }    

# Delete the message from the bucket
def deleteSMS(bucket,to_number):
    try:
        s3.delete_object(Bucket=bucket, Key=to_number)
    except:
        traceback.print_exc(file=sys.stdout)
        return {
            "state": "error",
            "error": "Could not delete the object."
        }