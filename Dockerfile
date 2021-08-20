FROM python:3.7

WORKDIR /stock

COPY requirements.txt .

RUN pip install -r requirements.txt

