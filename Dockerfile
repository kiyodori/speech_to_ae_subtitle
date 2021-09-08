FROM python:3

USER root

WORKDIR /app

RUN apt-get update
RUN apt-get -y install locales && \
  localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG=ja_JP.UTF-8 \
  LANGUAGE=ja_JP:ja \
  LC_AL=ja_JP.UTF-8 \
  TZ=JST-9 \
  TERM=xterm

RUN apt update
RUN apt -y upgrade
RUN apt install -y ffmpeg

RUN apt-get install -y vim less
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install poetry

COPY src/poetry.lock src/pyproject.toml ./
RUN poetry install
