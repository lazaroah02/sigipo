# Sigipo

Sistema Informático Integral de gestión del paciente Oncológico

![Django CI](https://github.com/UHo-GPDB/sigipo/actions/workflows/django-test.yml/badge.svg) ![pre-commit](https://github.com/UHo-GPDB/sigipo/actions/workflows/pre-commit.yml/badge.svg) ![Code Coverage](./coverage.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Python 3.10](https://img.shields.io/badge/python-3.10-brightgreen.svg)](https://www.python.org/downloads/release/python-3100/) ![Django](https://www.shields.io/badge/django-3.2-brightgreen) ![Interogate](./interrogate.svg)

## Configuración para el desarrollo

**(0)** En Windows.
Instalar [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install) (recomendado) o [Python](https://www.python.org/downloads/windows/).
De instalar Python directamente continue en la sección 2.

**(1)**. Instalar Python 3.10.

La mejor manera de hacer esto es con [pyenv](https://github.com/pyenv/pyenv).
Siga sus [instrucciones para configurarlo](https://realpython.com/intro-to-pyenv/) para su consola. También puede compilar directamente [Python](https://www.python.org/downloads/source/). Instale siempre la versión *más reciente* de Python.

**(2)** Cree un entorno virtual de Python y actívelo:
```sh
python3.10 -m venv venv
source venv/bin/activate
python -m pip install -U pip wheel
```

**(3)** Instalar las dependencias.

```sh
pip install -r requirements/development.txt
```

**(4)** Cree su archivo `.env` a partir del ejemplo:

```sh
cp .env.example .env
```

El archivo `.env` es para secretos que no están en el control de código fuente. Nunca agregue secretos reales a `.env.example`, solo valores ficticios.

**(5)** Cree su base de datos en PostgreSQL:

Edite el archivo `.env` de acuerdo con el nombre de su base de datos, contraseña y otras configuraciones.

**(6)** Configurar la base de datos de desarrollo:

```sh
python manage.py migrate
python manage.py loaddata province
python manage.py loaddata municipality
python manage.py loaddata topography
python manage.py loaddata morphology
```

**(7)** Ejecutar las pruebas:

```sh
pytest
```

Esto creará la base de datos y cargará algunos datos.

**(8)** Ejecutar el servidor de desarrollo.

```sh
python manage.py runserver
```

**(9)** Instalar [pre-commit](https://pre-commit.com/) en su repositorio local:

```sh
pre-commit install
```

Esto instala pre-commit en Git. Esta herramienta ejecuta verificaciones de formato y calidad del código, como Black y Flake8, cada vez que se realiza un 'commit'.

Verifique todos los archivos en el pase del repositorio con:

```sh
pre-commit run --all-files
```
