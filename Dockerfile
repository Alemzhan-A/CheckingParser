FROM python:3.8-slim

WORKDIR /app

# Установка git
RUN apt-get update && apt-get install -y git

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
