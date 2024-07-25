FROM python:3.8-slim

WORKDIR /app

# Установка git и других необходимых инструментов
RUN apt-get update && apt-get install -y git && apt-get clean

COPY requirements.txt requirements.txt

# Установка зависимостей по одной для диагностики
RUN pip install asyncio
RUN pip install git+https://github.com/ultrafunkamsterdam/nodriver.git
RUN pip install undetected-chromedriver

COPY . .

CMD ["python", "main.py"]
