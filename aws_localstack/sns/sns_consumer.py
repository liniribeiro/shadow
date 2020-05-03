import boto3

sqs = boto3.client("sqs", endpoint_url="http://localhost:4576")
queue_url = sqs.get_queue_url(QueueName="shadow-bts-local")


def get_messages(queue):
    response = sqs.receive_message(QueueUrl=queue, MaxNumberOfMessages=5,
                                   VisibilityTimeout=10, WaitTimeSeconds=1)
    return response


def read_messages():
    while True:
        try:
            messages = get_messages(queue_url)
            print(messages)
        except Exception as a:
            print(a)
            break


read_messages()