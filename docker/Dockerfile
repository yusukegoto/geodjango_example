FROM python:3.7

EXPOSE 8000

COPY docker/provision.sh /tmp/provision.sh
WORKDIR /tmp
RUN chmod +x provision.sh && ./provision.sh

COPY ./geo/requirements.txt /app/requirements.txt
COPY ./geo/requirements.dev.txt /app/requirements.dev.txt

WORKDIR /app
RUN pip install -r requirements.dev.txt

