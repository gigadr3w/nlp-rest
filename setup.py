from setuptools import setup
from setuptools.command.install import install

class PostInstall(install):
    def run(self):
        self.do_egg_install()

        import os
        os.system('apt-get update')
        os.system('apt-get --assume-yes install aspell-it')
        os.system('apt-get --assume-yes install aspell-fr')
        os.system('apt-get --assume-yes install aspell-de')
        os.system('apt-get --assume-yes install aspell-es')

        import nltk
        nltk.download('punkt')
        nltk.download('stopwords')

        import spacy
        from spacy.cli import download
        download('en_core_web_sm')
        download('fr_core_news_sm')
        download('de_core_news_sm')
        download('it_core_news_sm')
        download('es_core_news_sm')

setup(name='nlp-rest',
    version='1.0.1',
    author='Andrea Costa',
    description='A NLP rest service',
    long_description='Exposes endpoints for some natural language processing functions',
    python_requires='>=3.8.10, <4',
    install_requires=[
        'werkzeug==2.1.2',
        'flask==2.1.2',
        'flask_restx',
        'waitress',
        'nltk',
        'pyenchant==3.0.0a1',
        'wheel',
        'spacy'
    ],
    cmdclass={'install':PostInstall})