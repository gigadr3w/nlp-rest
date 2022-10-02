FROM python:3.8.10

WORKDIR /usr/src/app

RUN apt-get update 
RUN apt-get --assume-yes install libenchant1c2a
RUN apt-get --assume-yes install aspell-it
RUN apt-get --assume-yes install aspell-fr
RUN apt-get --assume-yes install aspell-de
RUN apt-get --assume-yes install aspell-es
RUN pip install Flask
RUN pip install waitress
RUN pip install werkzeug
RUN pip install nltk
RUN pip install pyenchant==3.0.0a1
RUN pip install talon==1.4.4
RUN pip install -U pip setuptools wheel
RUN pip install -U spacy
RUN python -m spacy download en_core_web_sm
RUN python -m spacy download fr_core_news_sm
RUN python -m spacy download de_core_news_sm
RUN python -m spacy download it_core_news_sm
RUN python -m spacy download es_core_news_sm

COPY app.py .
COPY enums.py .
COPY email_parser.py .

#local time Rome
RUN ln -fs /usr/share/zoneinfo/Europe/Rome /etc/localtime
RUN dpkg-reconfigure -f noninteractive tzdata

CMD ["python","./app.py", "prod"]