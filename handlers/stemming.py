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

class SnowballStemmerHandler():
    def __init__(self,language:SnowBallStemmerLanguageEnum) -> None:
        if language not in SnowballStemmers.keys():
            raise Exception('Selected snowball stemmer for ' + language.value + ' language, is not present')
        self._s = SnowballStemmers[language]
    def Handle(self, word) -> str:
        '''Stem the word'''
        try:
            return self._s.stem(word)
        except:
            return word