from models.sentence_analysis import SentenceAnalysisModel
from models.named_entity_recognition import NamedEntityRecognitionModel
from typing import List

class SentenceFullAnalysysModel():
    def __init__(self) -> None:
        self._sentence_analysis = list()
        self._ner = NamedEntityRecognitionModel()
    
    @property
    def sentence_analysis(self) -> List[SentenceAnalysisModel]:
        return self._sentence_analysis
    @sentence_analysis.setter
    def sentence_analysis(self, value:List[SentenceAnalysisModel]):
        self._sentence_analysis = value

    @property
    def ner(self) -> NamedEntityRecognitionModel:
        return self._ner
    @ner.setter
    def ner(self, value):
        self._ner = value

