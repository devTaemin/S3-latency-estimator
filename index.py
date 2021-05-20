import boto3
import time
report = [0 for col in range(5)]

#반드시 제출할때 지워야한다.
ACCESS_KEY = "AWS ACCESS KEY"
SECRET_KEY = "AWS SECRET KEY"
REGION = "ap-northeast-2"           #Asia/Seoul


# Boto3 Client
s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    #aws_session_token=SESSION_TOKEN,
    region_name=REGION
)


# Boto3 Resource
s3 = boto3.resource(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    #aws_session_token=SESSION_TOKEN,
    )


# Open data
temp = open('files/temp', 'rb')
data_1KB = open('files/file_1KB', 'rb')
data_10KB = open('files/file_10KB', 'rb')
data_1MB = open('files/file_1MB', 'rb')
data_10MB = open('files/file_10MB', 'rb')


# Store the variable of data
volume_list = [temp, data_1KB, data_10KB, data_1MB, data_10MB]
bucket_list = ["cloudclass-s3-demo-01",
                "cloudclass-s3-demo-02",
                "cloudclass-s3-demo-03",
                "cloudclass-s3-demo-04",
                "cloudclass-s3-demo-05",
                "cloudclass-s3-demo-06",
                "cloudclass-s3-demo-07",
                "cloudclass-s3-demo-08",
                "cloudclass-s3-demo-09",
                "cloudclass-s3-demo-10",
                "cloudclass-s3-demo-11",
                "cloudclass-s3-demo-12",
                "cloudclass-s3-demo-13",
                "cloudclass-s3-demo-14",
                "cloudclass-s3-demo-15"]


# Upload -> Download -> Delete: repetition(10)
# Upload: Change Bucket manually
for i in range(1): #10
    bucket_name = bucket_list[0]
    print(bucket_name)
    col = 0

    for idx in range(5):
        vol = volume_list[idx]
        start = time.time()
        s3.Bucket(bucket_name).put_object(Key=str(vol.name.split('/')[-1]), Body=vol)
        print(bucket_name + ": " + str(vol.name.split('/')[-1]) + " upload finish")
        latency = time.time() - start
        print("time :", latency)
        print('\n')
        report[col] += latency
        col = col + 1
    print('----------------------------\n')
    print(report)
    print('----------------------------\n')
print("result")
# for i in range(4):
#     report[i] = report[i]/10
print(report)


# Download: Change Bucket manually
for i in range(1): #10
    bucket_name = bucket_list[14]
    print(bucket_name)

    for idx in range(5):
        vol = volume_list[idx]
        file_name = str(vol.name.split('/')[-1])
        start = time.time()
        s3_client.download_file(bucket_name, file_name, file_name)
        latency = time.time() - start
        report[idx] += latency
        print("time :", latency)

print("result")
# for i in range(4):
#     report[i] = report[i]/10
print(report)


#Delete: Change Bucket manually
for i in range(1): #10
    bucket_name = bucket_list[14]
    print(bucket_name)

    for idx in range(5):
        vol = volume_list[idx]
        file_name = str(vol.name.split('/')[-1])
        start = time.time()
        s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        latency = time.time() - start
        report[idx] += latency
        print("time :", latency)


print("result")
# for i in range(4):
#     report[i] = report[i]/10
print(report)