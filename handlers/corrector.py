from factories.enchant import GetEnchantDict
from enums.correctors import CorrectorLanguageEnum

class CorrectorHandler():
    def __init__(self, language:CorrectorLanguageEnum):
        self._corrector = GetEnchantDict(language)

    def __correct(self, word):
        '''Correct the passed word with the firs found'''
        try:
            return self._corrector.suggest(word)[0]
        except:
            return word

    def Handle(self, word) -> str:
        '''Return the word if is correct, otherwise the corrected word'''
        if self._corrector.check(word):
            return word
        else:
            return self.__correct(word)