FROM python:3.8.9-slim-buster

COPY /requirements.txt /requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt

WORKDIR /weatherapp
COPY . .