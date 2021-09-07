import boto3
import os
from pathlib import Path

print('Loading function')

transcribe = boto3.client('transcribe')

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_name = event['Records'][0]['s3']['object']['key']
    region = os.environ.get('REGION')
    file_uri = f'https://{bucket_name}.s3-{region}.amazonaws.com/{object_name}'
    job_name = Path(object_name).stem

    transcribe.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={
            'MediaFileUri':file_uri
        },
        MediaFormat='wav',
        LanguageCode='ja-JP',
        OutputBucketName= os.environ.get('OUTPUT_BUCKET')
    )
