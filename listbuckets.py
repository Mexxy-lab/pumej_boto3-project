import boto3

client = boto3.client('s3')

response = client.list_buckets()

for pumej in response['Buckets']:
    print(pumej['Name'])
    print(pumej['CreationDate'])