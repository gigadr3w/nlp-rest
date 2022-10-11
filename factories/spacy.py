import spacy, logging, concurrent.futures 
from spacy.language import Language

from enums.spacy import SpacyLanguageEnum

Datasets = dict() 

def InitSpacy(language, dictionary):
    Datasets[language] = spacy.load(dictionary)

def GetSpacy(language:SpacyLanguageEnum) -> Language:
    if language not in Datasets.keys():
        raise Exception('Spacy not found for ' + language.name + ' language')

    return Datasets[language]

def InitSpacyAsync():
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(SpacyLanguageEnum)) as executor:
        for d in SpacyLanguageEnum:
            executor.submit(InitSpacy, d, d.value)
    logging.info("Spacy datatasets are ready!")