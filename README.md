# speech_to_ae_subtitle

Script for converting speech to subtitle.

## Requirements

* Adobe After Effects

## Setting

Create and launch a Docker container.

```bash
# Create and launch a Docker container
$ docker-compose up -d --build

# Run the container bash
$ docker-compose exec app bash
```

Create an AWS IAM user and two S3 buckets for file input and file output. Then, Set config and env files.

```bash
$ cp .aws/config.dev .aws/config
$ cp .env.dev .env
```

Create AWS lambda function for transcribing when wav file has uploaded to S3 input bucket.

* Set transcribe_function/lambda_function.py to AWS lambda function
* Specify an S3 input bucket for the lambda trigger
* Set the following two lambda environment variables
  * OUTPUT_BUCKET: AWS S3 output bucket
  * REGION: AWS S3 region
* Attach the following policy to lambda function
  * AmazonS3FullAccess
  * AmazonTranscribeFullAccess
  * CloudWatchLogsFullAccess

## Usage

### 1. Convert mp4 to wav

Place the mp4 files you want to convert in the input directory. The following command will output a wav file under the audio directory.

```bash
$ poetry run python converter.py test.mp4 test.wav
```

### 2. Upload wav to Amazon S3

Create S3 bucket. Then upload the wav file to the Amazon S3 bucket.

```bash
$ poetry run python uploader.py test.wav
```

### 3. Create AE script

### 4. Modify texts of AE script

### 5. Execute AE script

### 6. Export to mov

## Linter

black

```
$ poetry run black
```
