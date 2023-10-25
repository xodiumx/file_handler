FROM python:3.11.3-slim-bullseye

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y

RUN apt install -y build-essential libpq-dev

RUN pip3 install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

RUN ["chmod", "+x", "/app/docker/handler/entrypoint_app.sh"]

# CMD ["gunicorn", "file_handler.wsgi:application", "--bind", "0:8000"]
