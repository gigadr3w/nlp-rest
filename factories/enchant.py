import logging, enchant
from enchant import Dict

from enums.correctors import CorrectorLanguageEnum

Correctors = dict()

def InitEnchantDictionaries():
    '''Initialize enchant languages dictionary'''
    for l in CorrectorLanguageEnum:
        Correctors[l] = enchant.Dict(l.value)
        logging.debug('Enchant load ' + l.value + ' dictionary')
    logging.info('Correctors are ready!')

def GetEnchantDict(language:CorrectorLanguageEnum) -> Dict:
    if language not in Correctors.keys():
        raise Exception('Enchant dictionary not found for ' + language.name + ' language')

    return Correctors[language]