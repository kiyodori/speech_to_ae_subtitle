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

Set aws config files.

```bash
$ cp .aws/credentials.dev .aws/credentials
$ cp .aws/config.dev .aws/config
```

## Usage

### 1. Convert mp4 to wav

First, place the mp4 files you want to convert in the input directory. Then, convert it to a wav file by specifying the file name under the audio directory.

```bash
$ python convert.py input/test.mp4 audio/test.wav
```

### 2. Upload wav to Amazon S3

### 3. Create AE script

### 4. Modify texts of AE script

### 5. Execute AE script

### 6. Export to mov
