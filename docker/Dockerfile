FROM python:3.5

EXPOSE 8000

COPY docker/provision.sh /tmp/provision.sh
WORKDIR /tmp
RUN chmod +x provision.sh && ./provision.sh

COPY requirements.txt /app/requirements.txt
COPY requirements.dev.txt /app/requirements.dev.txt

WORKDIR /app
RUN pip install -r requirements.dev.txt

