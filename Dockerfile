FROM python:3.12-slim

WORKDIR /app

# Копирование файла с зависимостями
COPY pyproject.toml poetry.lock ./

# Установка Poetry
RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-dev --no-root

COPY . .

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver"]
