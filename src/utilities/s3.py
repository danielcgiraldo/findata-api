import os
import boto3

def upload_file(file_to_upload, location_to_upload):

    # Create a session with your AWS credentials
    session = boto3.Session(
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

    # Create an S3 client
    s3 = session.client('s3')

    # Define the cache control value for one month (in seconds)
    cache_control = "max-age=2592000"  # 30 days * 24 hours/day * 60 minutes/hour * 60 seconds/minute

    # Upload the file to S3 with cache control headers
    s3.upload_file(file_to_upload, os.getenv("AWS_S3_BUCKET"), location_to_upload, ExtraArgs={'CacheControl': cache_control, 'ACL': 'public-read'})

    return True
