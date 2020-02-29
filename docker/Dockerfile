FROM python:3.5

EXPOSE 8000

COPY docker/provision.sh /tmp/provision.sh
WORKDIR /tmp
RUN chmod +x provision.sh && ./provision.sh

COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock

WORKDIR /app
RUN pipenv install
