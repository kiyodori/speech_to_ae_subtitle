from dotenv import load_dotenv
load_dotenv()

import os

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
S3_INPUT_BUCKET_NAME = os.getenv('S3_INPUT_BUCKET_NAME')
