import boto3

client = boto3.client('s3')

response = client.list_objects(
    Bucket='pumej-bucket'
)

for object in response['Contents']:
    print(object['Key'], object['Owner'], object['ETag'])