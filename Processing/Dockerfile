FROM python:latest

LABEL maintainer = "sschlegel1@my.bcit.ca"

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install -y sqlite3

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8100

CMD python create_database.py && python app.py
