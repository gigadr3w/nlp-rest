A Nlp-rest service 
========================

This is a basic nlp-rest service made in python flask with which you can handle some different Natural Language Processing functions such as:

* correct statements, using
    - [libenchant1c2a](https://www.ubuntuupdates.org/package/core/focal/universe/base/libenchant1c2a) a wrapper library for various spell checker engines
    - various [aspell](https://ftp.gnu.org/gnu/aspell/dict/0index.html) language dictionaries
* tokenize statements
* clear statements from stop words
* lemmantization, using
    - [spacy](https://spacy.io/)
* stemming

Requirements 
========================

1. At first I raccomend to build and use a python virtual environment to not modify your own global environment (_note I'm using VSCode on Ubuntu 20.04 OS_). To do this, once cloned the .git repo, open VSCode and in its terminal type  


```Shell
python3 -m venv /path/to/new/virtual/environment
```

To use the virtual environment just created type 

```Shell
source /path/to/new/virtual/environment/bin/activate
```

For more informations about virtual environment you can take a look [here](https://docs.python.org/3/library/venv.html)

2. Second, you need to set properly your virtual environment. Once you're in:

- Install package dependencies typing

```Shell
pip install -r requirements.txt
```

Now, we have to set up the enchant wrapper and some aspell dictionaries (I've opted for IT, EN, FR, DE, and ES)

```Shell
sudo bash -c 'apt-get update && /
apt-get --assume-yes install libenchant1c2a && /
apt-get --assume-yes install aspell-it && /
apt-get --assume-yes install aspell-fr && /
apt-get --assume-yes install aspell-de && /
apt-get --assume-yes install aspell-es'
```

At at the end, set up other spacy dicionaries

```Shell
python3 -m spacy download en_core_web_sm && 
python3 -m spacy download fr_core_news_sm && 
python3 -m spacy download de_core_news_sm && 
python3 -m spacy download it_core_news_sm && 
python3 -m spacy download es_core_news_sm
```

How to use 
========================
