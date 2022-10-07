import logging, enchant
from enums.correctors import CorrectorLanguageEnum

Correctors = dict()

def InitCorrectors():
    '''Initialize enchant languages dictionary'''
    for l in CorrectorLanguageEnum:
        Correctors[l] = enchant.Dict(l.value)
        logging.debug('Enchant load ' + l.value + ' dictionary')
    logging.info('Correctors are ready!')

class CorrectorHandler():
    def __init__(self, language:CorrectorLanguageEnum):
        if language not in Correctors.keys():
            raise Exception('No corrector found for ' + language.name + ' language')
        self._corrector = Correctors[language]
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