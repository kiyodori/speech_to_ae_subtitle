import boto3
import fire

def upload(file, bucket):
  s3 = boto3.resource('s3')
  data = open(f'audio/{file}', 'rb')
  s3.Bucket(bucket).put_object(Key=file, Body=data)

if __name__ == '__main__':
  fire.Fire(upload)
