from enums.spacy import SpacyLanguageEnum
from handlers.spacy import Datasets

class SpacyLemmatizerHandler():
    def __init__(self, language:SpacyLanguageEnum) -> None:
        self._l = Datasets[language]
    
    def LemmatizeWord(self, word:str) -> str:
        '''Returns the lemmatized word'''
        w = self._l(word)
        return w._lemma
    
    def LemmatizeSentence(self, sentence:str) -> list:
        '''Returns the sentence with lemmatized word'''
        words = self._l(sentence)
        return str.join(' ',[w.lemma_ for w in words])