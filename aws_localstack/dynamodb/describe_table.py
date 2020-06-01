import boto3


def describe_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.client('dynamodb', endpoint_url="http://localhost:4569")

    table = dynamodb.describe_table(
        TableName='Movies'
    )
    print(table)


if __name__ == '__main__':
    describe_table()
