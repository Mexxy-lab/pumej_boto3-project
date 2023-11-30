import boto3

client = boto3.client('s3')

#response = client.delete_bucket(
    #Bucket='pumej-bucket',
#)

client = boto3.client('s3')

#response = client.delete_bucket(
    #Bucket='sammi12-bucket',
#)

client = boto3.client('s3')

response = client.delete_bucket(
    Bucket='fechi-bucket',
)

client = boto3.client('s3')

response = client.delete_bucket(
    Bucket='paul12-bucket',
)

print(response)