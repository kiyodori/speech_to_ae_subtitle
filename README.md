# speech_to_subtitle

Script for converting speech to subtitle.

## Requirements

* Premiere Pro

## Setting

```bash
# Create and launch a Docker container
$ docker-compose up -d --build

# Run the container bash
$ docker-compose exec python3 bash
```

## Usage

### 1. Convert mp4 to wav

First, place the mp4 files you want to convert in the input directory. Then, convert it to a wav file by specifying the file name under the audio directory.

```bash
$ python convert.py input/test.mp4 audio/test.wav
```
