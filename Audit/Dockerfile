FROM python:latest

LABEL maintainer = "sschlegel1@my.bcit.ca"

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8110

CMD python app.py
