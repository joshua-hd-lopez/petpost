import json
import uuid
import os 
import boto3 
from django.conf import settings

s3 = boto3.client('s3', region_name=settings.AWS_REGION)


def load():
    if not settings.PET_DATA.exists():
        return []
    with open(settings.PET_DATA, 'r') as f:
        return json.load(f)    


def save(pets):
    with open(settings.PET_DATA, 'w') as f:
        json.dump(pets, f, indent=2)

def upload(file, filename):
    key = f'{uuid.uuid4()}_{filename}'
    s3.upload_fileobj(
        Fileobj = file, 
        Bucket = settings.S3_BUCKET,
        Key = key,
        ExtraArgs = {"ACL": "public-read", "ContentType": file.content_type}

    )

    return f"https://{settings.S3_BUCKET}.s3.amazonaws.com/{key}"