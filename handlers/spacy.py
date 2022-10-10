import spacy, logging, concurrent.futures 
from typing import List

from enums.spacy import SpacyLanguageEnum
from models.named_entity_recognition import NamedEntityRecognitionModel

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
    def GetNER(self, sentence:str) -> List[NamedEntityRecognitionModel]:
        '''Returns a list of Named Entity Recognition within sentence'''
        words = self._l(sentence)
        items = list()
        for ent in words.ents:
            item = NamedEntityRecognitionModel()
            item.text = ent.text
            item.start = ent.start_char
            item.end = ent.end_char
            item.entity = ent.label_
            items.append(item)

        return items