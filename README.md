A basic Nlp-rest service 
========================

This is a basic nlp-rest service made in python flask with which you can handle some different Natural Language Processing functions, using some different libraries I've found very usefull, such as:

* correct statements
* tokenize statements
* clear statements from stop words
* lemmantization
* stemming

How to use 
========================

1. At first is raccomended to build and use a python virtual environment to not modify your own global environment. To do this type 


```Shell
python3 -m venv /path/to/new/virtual/environment
```

or

```Shell
python -m venv /path/to/new/virtual/environment
```

Once created, to use the virtual environment (_note, it may depend on your OS, in my case I'm using an Ubuntu_) type 

```Shell
source /path/to/new/virtual/environment/bin/activate
```

i.e. under Windows PowerShell you may need to type something like that

```Shell
/path/to/new/virtual/environment/Scripts/activate
```

For more informations about virtual environment you can take a look [here](https://docs.python.org/3/library/venv.html)

2. Second, you need to set properly your virtual environment. Once you're in install some libraries typing:

```Shell
sudo bash -c 'apt-get update && /
apt-get --assume-yes install libenchant1c2a && /
apt-get --assume-yes install aspell-it && /
apt-get --assume-yes install aspell-fr && /
apt-get --assume-yes install aspell-de &&/
apt-get --assume-yes install aspell-es '
```

```Shell
pip install Flask && /
pip install waitress && /
pip install werkzeug && /
pip install nltk && /
pip install pyenchant==3.0.0a1 && /
pip install talon==1.4.4 && /
pip install -U pip setuptools wheel && /
pip install -U spacy && /
python3 -m spacy download en_core_web_sm && /
python3 -m spacy download fr_core_news_sm && /
python3 -m spacy download de_core_news_sm && /
python3 -m spacy download it_core_news_sm && /
python3 -m spacy download es_core_news_sm
```