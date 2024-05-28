FROM python:3.10-slim-bullseye

RUN apt-get update && \
    apt-get upgrade -y

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8

WORKDIR /root/Service

COPY requirements.txt /root/Service/

RUN pip install -r requirements.txt

ADD . /root/Service

CMD gunicorn -b :7500 main:app --workers 3 --threads 10 --worker-class gthread --access-logfile -