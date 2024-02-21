FROM python:3.12 as requirements-stage

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.12

WORKDIR /code

COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./controllers /code/controllers
COPY ./models /code/models
COPY ./schemas /code/schemas
COPY ./tests /code/tests
COPY ./views /code/views
COPY ./main.py /code/

EXPOSE 8000

CMD ["python", "main.py"]