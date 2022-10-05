A Nlp-rest service 
========================

This is a basic rest service made with python [flask](https://flask.palletsprojects.com/en/2.2.x/) with an easy Swagger interface made with [flask_restx](https://flask-restx.readthedocs.io/en/latest/), with which you can handle some different Natural Language Processing functions such as:

* correct statements, using
    - [pyenchant](https://pyenchant.github.io/pyenchant/) a library for spellchecking based on [Enchant](https://abiword.github.io/enchant/) thant uses some [aspell](https://ftp.gnu.org/gnu/aspell/dict/0index.html) language dictionaries
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

Once you've created the virtual environment VSCode should prompt a message for select it as default python interpreter. If not with the VSCode command prompt (in my case `Ctrl-Shift-P`) choose `Python: select interpreter` and next select the interpreter in your virtual environment

Then, in the VSCode terminal activate the virtual environment typing 

```Shell
source /path/to/new/virtual/environment/bin/activate
```

For more informations about virtual environment you can take a look [here](https://docs.python.org/3/library/venv.html)

2. Second, you need to set properly your virtual environment installing all the dependencies : there is a setup.py file, open it and take a look. Once you're in the virtual environment type

```Shell
pip install .
```

How to use 
========================

Once you've installed all the dependencies, you can run and debug the solution: enjoy!