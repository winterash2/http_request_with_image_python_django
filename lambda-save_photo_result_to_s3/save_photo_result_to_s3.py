import boto3
import json
import os
import logging


#----------------------------------------------------------------------
'''
DEBUG	    10	(주로 문제 해결을 할 때 필요한) 자세한 정보.
INFO    	20	작업이 정상적으로 작동하고 있다는 확인 메시지.
WARNING 	30	예상하지 못한 일이 발생하거나, 발생 가능한 문제점을 명시. (e.g. ‘disk space low’) 작업은 정상적으로 진행.
ERROR	    40	프로그램이 함수를 실행하지 못 할 정도의 심각한 문제.
CRITICAL	50	프로그램이 동작할 수 없을 정도의 심각한 문제.
'''
logging.basicConfig(level=logging.INFO)
#----------------------------------------------------------------------
ACCESS_ID = ''
ACCESS_KEY = ''
BUCKET_NAME = "photo-product-line-1"
FOLDER_NAME = '2020-12-02'
FILE_NAME = '2020-12-02-05-12-01-1.jpg'

s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_ID,
    aws_secret_access_key= ACCESS_KEY
)
base_path = os.getcwd()

#----------------------------------------------------------------------
def get_bucket_list():
    # 버킷의 목록을 출력하는 함수
    logging.info('--get_file_list_of_bucket--')
    for bucket in s3.buckets.all():
        print(bucket.name)
    return


def create_folder_in_bucket(bucket_name, folder_name):
    # 버킷 안에 특정 이름의 폴더를 생성하는 함수
    logging.info('--get_file_list_of_bucket--')
    bucket = s3.Bucket(bucket_name)
    bucket.put_object(
        Key = folder_name + '/'
    )


def get_file_list_of_bucket(bucket_name):
    # 버킷 안의 파일 목록을 반환하는 함수, 반환 형태는 list임
    logging.info('--get_file_list_of_bucket--')
    bucket = s3.Bucket(BUCKET_NAME)
    response = bucket.objects.all()
    key_list = []
    for file in response:
        key_list.append(file.key)
    print(key_list)
    return key_list


def put_file_to_bucket(bucket_name, folder_name, file_name):
    logging.info('---put_file_to_bucket---')
    bucket = s3.Bucket(BUCKET_NAME)
    data = open(file_name, 'rb')
    response = bucket.put_object(Key=folder_name + '/' + file_name, Body=data)
    print(response)
    return response

#----------------------------------------------------------------------

# create_folder_in_bucket(BUCKET_NAME, '2020-12-02') #정상 동작 확인함
get_bucket_list()
get_file_list_of_bucket(BUCKET_NAME)
put_file_to_bucket(BUCKET_NAME, FOLDER_NAME, FILE_NAME)


# transactionToUpload = { 임의의 딕트 }
# uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))