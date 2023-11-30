import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='pumej-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1',
    },
)

response = client.create_bucket(
    Bucket='sammi12-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1',
    },
)

response = client.create_bucket(
    Bucket='fechi-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1',
    },
)

response = client.create_bucket(
    Bucket='paul12-bucket',
    CreateBucketConfiguration={
        'LocationConstraint': 'eu-west-1',
    },
)

print(response)