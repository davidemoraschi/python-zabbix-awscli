#!/usr/bin/python
'''
# Testing SNS service
'''

import boto3

# Create an SNS client
sns = boto3.client('sns')

# Create a new topic
response = sns.create_topic(
    Name='ds6-failure-topic'
)

# Print the topic ARN
print(response['TopicArn'])

# # Subscribe an email address to the topic
# response = sns.subscribe(
#     TopicArn='arn:aws:sns:eu-west-1:816247855850:ds6-failure-topic',
#     Protocol='email',
#     Endpoint='davide.moraschi@straumann.com'
# )

# # Print the subscription ARN
# print(response['SubscriptionArn'])

# Publish a message to the topic
response = sns.publish(
    TopicArn='arn:aws:sns:eu-west-1:816247855850:ds6-failure-topic',
    Message='This is a test message'
)

# Print the message ID
print(response['MessageId'])
