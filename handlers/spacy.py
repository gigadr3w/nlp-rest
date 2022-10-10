import spacy, logging, concurrent.futures 

from enums.spacy import SpacyLanguageEnum

Datasets = dict()

def InitSpacy(language, dictionary):
    Datasets[language] = spacy.load(dictionary)
    logging.debug("SpaCy load " + dictionary + " dictionary for " + language + " language.")

def InitSpacyAsync():
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(SpacyLanguageEnum)) as executor:
        for d in SpacyLanguageEnum:
            executor.submit(InitSpacy, d, d.value)
    logging.info("Spacy datatasets are ready!")

class SpacyHandler():
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