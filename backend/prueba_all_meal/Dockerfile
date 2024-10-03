FROM python:3.10.12

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN groupadd -g 1000 celery && useradd -u 1000 -g 1000 -s /bin/bash celery
USER celery

COPY .env /code/.env

ENV CELERY_BROKER_URL=redis://redis:6379/0
ENV CELERY_RESULT_BACKEND=redis://redis:6379/0

CMD ["sh", "-c", "python manage.py makemigrations && python manage.py migrate", "python", "manage.py", "runserver", "0.0.0.0:8000"]
