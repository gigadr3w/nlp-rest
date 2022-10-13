from typing import Text
from enums.text_type import TextTypeEnum
from enums.pos import POSTypeEnum

class SentenceAnalysisModel():
    def __init__(self) -> None:
        self._text = str()
        self._language = str()
        self._start = 0
        self._end = 0
        self._start_sentence = False
        self._end_sentence = False
        self._pos = POSTypeEnum.X
        self._lemma = str()
        self._corrected_text = str()
        self._stem = str()
        self._morphological = dict() 
        self._shape = str()
        self._text_type = TextTypeEnum.string
        self._is_stopword = False
    
    @property 
    def text(self) -> str:
        '''Text content'''
        return self._text
    @text.setter
    def text(self, value):
        self._text = value

    @property 
    def language(self) -> str:
        '''The language of the text'''
        return self._language
    @language.setter
    def language(self, value):
        self._language = value

    @property 
    def start(self) -> int:
        return self._start
    @start.setter
    def start(self, value):
        self._start = value

    @property 
    def end(self) -> int:
        return self._end
    @end.setter
    def end(self, value):
        self._end = value

    @property 
    def start_sentence(self) -> bool:
        '''The word start the sentence?'''
        return self._start_sentence
    @start_sentence.setter
    def start_sentence(self, value):
        self._start_sentence = value

    @property 
    def end_sentence(self) -> bool:
        '''The word end the sentence?'''
        return self._end_sentence
    @end_sentence.setter
    def end_sentence(self, value):
        self._end_sentence = value

    @property 
    def pos(self) -> POSTypeEnum:
        '''Part-of-speech'''
        return self._pos
    @pos.setter
    def pos(self, value):
        self._pos = value

    @property 
    def lemma(self) -> str:
        '''Base form of the text content'''
        return self._lemma
    @lemma.setter
    def lemma(self, value):
        self._lemma = value

    @property 
    def corrected_text(self) -> str:
        '''Text content corrected'''
        return self._corrected_text
    @corrected_text.setter
    def corrected_text(self, value):
        self._corrected_text = value

    @property 
    def stem(self) -> str:
        '''Stem form of the text content'''
        return self._stem
    @stem.setter
    def stem(self, value):
        self._stem = value

    @property 
    def morphological(self) -> dict:
        '''Morphological analysis'''
        return self._morphological
    @morphological.setter
    def morphological(self, value):
        self._morphological = value

    @property 
    def shape(self) -> str:
        '''The shape of the text (i.e. Name Xxxx, U.S.A. X.X.X. etc.)'''
        return self._shape
    @shape.setter
    def shape(self, value):
        self._shape = value

    @property 
    def text_type(self) -> TextTypeEnum:
        '''Is it an email, an url or a currency?'''
        return self._text_type
    @text_type.setter
    def text_type(self, value):
        self._text_type = value

    @property 
    def is_stopword(self) -> bool:
        '''Is a stopword'''
        return self._is_stopword
    @is_stopword.setter
    def is_stopword(self, value):
        self._is_stopword = value 
