FROM python:3.11.9-bookworm

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN pip install --upgrade pip "poetry==2.1.1"

RUN poetry config virtualenvs.create false --local

RUN poetry install

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]