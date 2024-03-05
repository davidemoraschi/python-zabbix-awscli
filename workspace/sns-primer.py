#!/usr/bin/python
'''
# Testing SNS service
'''

import boto3
import tabulate

try:
    x = 1/0
    print(x)

except Exception as exc:
    # Create an SNS client
    sns = boto3.client('sns')

    # Create a new topic
    response = sns.create_topic(
        Name='ds6-failure-topic'
    )

    # Print the topic ARN
    print(response['TopicArn'])

    # Publish a message to the topic
    response = sns.publish(
        TopicArn='arn:aws:sns:eu-west-1:816247855850:ds6-failure-topic',
        Message=(tabulate.tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age'], tablefmt='psql', showindex=False))
    )

    # Print the message ID
    print(response['MessageId'])
    
