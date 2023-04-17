FROM python:3.10.5-alpine

ARG ENV

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=config.settings.${ENV}

WORKDIR /code

RUN apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add mariadb-dev

# Install requirements
RUN pip install --upgrade pip
COPY requirements/* /code/requirements/
RUN pip install -r requirements/${ENV}.txt

COPY . /code/

RUN if [ "$ENV" = "production" ] ; then mkdir -p /code/staticfiles ; fi
RUN if [ "$ENV" = "production" ] ; then mkdir -p /code/mediafiles ; fi

EXPOSE 8000
