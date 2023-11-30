import boto3

client = boto3.client('s3')

s3 = boto3.client('s3')

#s3.upload_file('C:/Users/pumej/Documents/Emeka_Portfolio/images/logo.jpg', 'pumej-bucket', 'pumej/logo.jpg')

s3.upload_file('C:/Users/pumej/Documents/Emeka_Portfolio/images/logo.jpg', 'fechi-bucket', 'logo.jpg')