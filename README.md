# sigipo

Sistema Informático Integral de gestión del paciente Oncológico

![Django CI](https://github.com/UHo-GPDB/sigipo/actions/workflows/django-test.yml/badge.svg)

![pre-commit](https://github.com/UHo-GPDB/sigipo/actions/workflows/pre-commit.ym/badge.svg)

## License

Distributed under the terms of the [Not open source](LICENSE) license,

## Running in development mode

First install the dependencies

    pip install -r requirements/development.txt

Then run the development server

    python manage.py runserver --settings=config.settings.development
