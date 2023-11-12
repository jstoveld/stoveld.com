FROM python:3.10-alpine

WORKDIR /app

COPY . .

RUN ls

# Uncomment the following line if you have a requirements.txt file
RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "app.py"]