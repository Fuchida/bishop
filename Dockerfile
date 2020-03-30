FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./app /app
COPY Pipfile.lock /app
COPY Pipfile /app

# These should really be set in container services for AWS,GCP or Azure
ENV S3_BUCKET_NAME=
ENV AWS_ACCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=

WORKDIR /app

RUN pip install pipenv
RUN pipenv install --ignore-pipfile --system