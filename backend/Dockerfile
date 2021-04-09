FROM python:3-buster

RUN apt-get -y update && apt-get -y upgrade

COPY requirements.txt /
RUN pip3 install -r requirements.txt

COPY . /app
WORKDIR /app

RUN chmod +x runserver.py
ENTRYPOINT ["python3", "./runserver.py"]
