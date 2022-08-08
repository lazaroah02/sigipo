FROM python:3.10.5-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings.production

WORKDIR /code

RUN apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add mariadb-dev

# Install requirements
RUN pip install --upgrade pip
COPY requirements/* /code/requirements/
RUN pip install -r requirements/production.txt

COPY . /code/

RUN mkdir -p /code/staticfiles
RUN mkdir -p /code/mediafiles

EXPOSE 8000
