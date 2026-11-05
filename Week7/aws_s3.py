
import boto3
import json
from pprint import pprint as pp
from botocore.exceptions import ClientError

# =====================================
# 1. Connect to AWS
# =====================================

session = boto3.Session()

print("AWS Region:", session.region_name)

# Test AWS identity using STS
sts = session.client('sts')
identity = sts.get_caller_identity()

print("\nAWS Identity:")
print("Account:", identity['Account'])
print("User:", identity['Arn'])

# =====================================
# 2. Connect to Amazon S3
# =====================================

s3_client = session.client('s3')
s3_resource = session.resource('s3')

# =====================================
# 3. List available S3 buckets
# =====================================

print("\nAvailable S3 buckets:")

response = s3_client.list_buckets()

for bucket in response['Buckets']:
    print(bucket['Name'])

# =====================================
# 4. Create a Python dictionary
# =====================================

dict_to_upload = {
    'name': 'Salma',
    'course': 'Data 606',
    'subject': 'AWS Boto3',
    'service': 'Amazon S3'
}

print("\nPython dictionary:")
pp(dict_to_upload)

# =====================================
# 5. Convert dictionary to JSON
# =====================================

json_filename = 'data.json'

with open(json_filename, 'w') as jsonfile:
    json.dump(dict_to_upload, jsonfile, indent=4)

print("\nJSON file created successfully!")

# =====================================
# 6. Read JSON back into Python
# =====================================

with open(json_filename, 'r') as jsonfile:
    json_data = json.load(jsonfile)

print("\nJSON converted back into Python:")
pp(json_data)

print("Data type:", type(json_data))

# =====================================
# 7. Upload JSON file to S3
# =====================================

# Replace with your trainer's confirmed bucket name
bucket_name = 'YOUR_ASSIGNED_BUCKET'

s3_key = 'Data606/Test/salma.json'

try:
    s3_client.upload_file(
        Filename=json_filename,
        Bucket=bucket_name,
        Key=s3_key
    )

    print("\nUpload successful!")

    # =====================================
    # 8. Verify uploaded object
    # =====================================

    object_info = s3_client.head_object(
        Bucket=bucket_name,
        Key=s3_key
    )

    print("Object uploaded:", s3_key)
    print("File size:", object_info['ContentLength'], "bytes")

except ClientError as error:
    print("\nS3 operation failed:")
    print(error.response['Error']['Code'])
    print(error.response['Error']['Message'])
