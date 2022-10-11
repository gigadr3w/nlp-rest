import logging
from nltk.stem import SnowballStemmer

from enums.stemming import SnowBallStemmerLanguageEnum

SnowballStemmers = dict()

def InitSnowballStemmers():
    '''Initialize stemmer languages dictionary'''
    for language in SnowBallStemmerLanguageEnum:
        SnowballStemmers[language] = SnowballStemmer(language.value)
        logging.debug('Stemmer configured ' + language.value + ' dictionary')
    logging.info('Snowball stemmer is ready!')

def GetSnowballStemmer(language:SnowBallStemmerLanguageEnum) -> SnowballStemmer:
    if language not in SnowballStemmers.keys():
        raise Exception('Snowball Stemmer not found for ' + language.name + ' language')

    return SnowballStemmers[language]