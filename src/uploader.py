import boto3
import fire
import config

def upload(file):
  s3 = boto3.resource('s3',
    aws_access_key_id=config.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY)
  data = open(f'audio/{file}', 'rb')
  s3.Bucket(config.S3_INPUT_BUCKET_NAME).put_object(Key=file, Body=data)

if __name__ == '__main__':
  fire.Fire(upload)
