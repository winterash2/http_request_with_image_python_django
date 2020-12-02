import json
import boto3
import os

#----------------------------------------------------------------------
ACCESS_ID = os.environ.get('ACCESS_ID')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
BUCKET_NAME = "photo-product-line-1"

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_ID,
    aws_secret_access_key= ACCESS_KEY
)
#----------------------------------------------------------------------
def get_bucket_list():
    # 버킷의 목록을 출력하는 함수
    for bucket in s3.buckets.all():
        print(bucket.name)
    return
#----------------------------------------------------------------------
def lambda_handler(event, context):
    
    body = event['body']
    
    # bucket = s3.Bucket("photo-product-line-1")
    # response = bucket.put_object(Key='cat.jpg', Body=event['body'])

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
