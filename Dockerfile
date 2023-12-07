FROM python:3.11-alpine
WORKDIR /app

COPY ./requirements.txt /code/requirements.txt
RUN pip install flet

COPY . /app

EXPOSE 8080
CMD ["python", "main.py"]
