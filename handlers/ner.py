from typing import List

from enums.spacy import SpacyLanguageEnum
from models.named_entity_recognition import NamedEntityRecognitionModel
from factories.spacy import GetSpacy

class SpacyNERHandler():
    def __init__(self, language:SpacyLanguageEnum) -> None:
        self._l = GetSpacy(language)
    
    def NamedEntityRecognition(self, sentence:str) -> List[NamedEntityRecognitionModel]:
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