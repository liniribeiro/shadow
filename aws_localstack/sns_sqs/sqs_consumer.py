import boto3

sqs = boto3.client("sqs", endpoint_url="http://localhost:4576")
queue_url = sqs.get_queue_url(QueueName="shadow-bts-local")['QueueUrl']


def get_messages(queue):
    response = sqs.receive_message(QueueUrl=queue, MaxNumberOfMessages=10,
                                   VisibilityTimeout=10, WaitTimeSeconds=1)
    return response


def read_messages():
    while True:
        try:
            entries = []
            messages = get_messages(queue_url)
            for message in messages['Messages']:
                print(messages)
                entries.append(
                    {'Id': message.get('MessageId'), 'ReceiptHandle': message.get('ReceiptHandle')})
            sqs.delete_message_batch(QueueUrl=queue_url, Entries=entries)
        except Exception as a:
            print(a)
            break


read_messages()