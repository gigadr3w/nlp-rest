import logging, enchant
from enums.correctors import CorrectorLanguageEnum

Correctors = dict()

def InitCorrectors():
    for l in CorrectorLanguageEnum:
        Correctors[l] = enchant.Dict(l.value)
        logging.debug("Enchant load " + l.value + " dictionary")
    logging.info("Correctors are ready!")