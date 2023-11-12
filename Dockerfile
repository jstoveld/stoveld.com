FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN pip install Flask

CMD ["python", "app.py"]