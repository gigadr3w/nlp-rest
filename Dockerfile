FROM python:3.8.10

WORKDIR /usr/src/app

COPY . .

RUN python setup.py install

CMD ["python","./app.py", "prod"]