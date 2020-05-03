import json

import boto3

sns = boto3.client("sns", endpoint_url="http://localhost:4575")

topic_arn = sns.create_topic(Name='shadow-kpop-local')['TopicArn']

bts_subscription_arn = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='sqs',
    Endpoint='arn:aws:sqs:us-east-1:000000000000:shadow-bts-local'
)['SubscriptionArn']

ui_subscription_arn = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='sqs',
    Endpoint='arn:aws:sqs:us-east-1:000000000000:shadow-ui-local'
)['SubscriptionArn']


sns.set_subscription_attributes(
    SubscriptionArn=bts_subscription_arn,
    AttributeName='FilterPolicy',
    AttributeValue='{"channel": "bts"}'
)

sns.set_subscription_attributes(
    SubscriptionArn=ui_subscription_arn,
    AttributeName='FilterPolicy',
    AttributeValue='{"channel": "ui"}'
)


def publish_message(message: str, channel: str):
    return sns.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=channel
    )


message = {
    'album': '7'
}

print(publish_message(json.dumps(message), "bts"))



# topic = "arn:aws:sns:us-east-1:000000000000:shadow-kpop-local"
# def publish_message(topic_arn: str, message: str, channel: str):
#     return sns.publish(
#         TopicArn=topic_arn,
#         Message=message,
#         Subject=channel
#     )
# message = {
#     'album': '7'
# }
#
# sns_filter = 'bts'
#
# print(publish_message(topic, json.dumps(message), sns_filter))
