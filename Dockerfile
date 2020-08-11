FROM python:3

ENV PYTHONUNBUFFERED 1

COPY . /ihateironing

WORKDIR /ihateironing

RUN pip install  -r requirements.txt

WORKDIR /ihateironing/winterfell
