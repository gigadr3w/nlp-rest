from factories.snowballstemmer import GetSnowballStemmer
from enums.stemming import SnowBallStemmerLanguageEnum

class SnowballStemmerHandler():
    
    def __init__(self,language:SnowBallStemmerLanguageEnum) -> None:
        self._s = GetSnowballStemmer(language)

    def Handle(self, word) -> str:
        '''Stem the word'''
        try:
            return self._s.stem(word)
        except:
            return word