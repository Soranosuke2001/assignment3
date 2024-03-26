FROM python:latest

LABEL maintainer = "sschlegel1@my.bcit.ca"

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8090

CMD python create_database.py && python app.py
