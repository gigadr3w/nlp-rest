import spacy, logging, concurrent.futures 

from enums.spacy import SpacyLanguageEnum

Datasets = dict()

def InitSpacy(language, dictionary, logging):
    Datasets[language] = spacy.load(dictionary)
    logging.debug("SpaCy load " + dictionary + " dictionary for " + language + " language.")

def InitSpacyAsync():
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(SpacyLanguageEnum)) as executor:
        for d in SpacyLanguageEnum:
            executor.submit(InitSpacy, d, d.value, logging)
    logging.info("Spacy datatasets are ready!")