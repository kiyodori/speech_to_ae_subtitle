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
$ docker-compose exec python3 bash
```

Create an AWS IAM and set aws config files.

```bash
$ cp .aws/credentials.dev .aws/credentials
$ cp .aws/config.dev .aws/config
```

## Usage

### 1. Convert mp4 to wav

Place the mp4 files you want to convert in the input directory. The following command will output a wav file under the audio directory.

```bash
$ python converter.py test.mp4 test.wav
```

### 2. Upload wav to Amazon S3

Create S3 bucket. Then upload the wav file to the Amazon S3 bucket.

```bash
$ python uploader.py test.wav my-bucket
```

### 3. Create AE script

### 4. Modify texts of AE script

### 5. Execute AE script

### 6. Export to mov
