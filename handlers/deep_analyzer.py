from enums.sentence_analysis import DeepAnalyzerLanguageEnum
from enums.correctors import CorrectorLanguageEnum
from enums.stemming import SnowBallStemmerLanguageEnum
from enums.spacy import SpacyLanguageEnum
from enums.pos import POSTypeEnum
from enums.text_type import TextTypeEnum
from models.sentence_analysis import SentenceAnalysisModel

from models.sentence_full_analysis import SentenceFullAnalysysModel

from factories.spacy import GetSpacy

from handlers.corrector import CorrectorHandler
from handlers.stemming import SnowballStemmerHandler
from handlers.ner import SpacyNERHandler

class DeepAnalyzerHandler():
    def __init__(self, language: DeepAnalyzerLanguageEnum) -> None:
        self._corrector = CorrectorHandler(CorrectorLanguageEnum[language.name])
        self._stemmer = SnowballStemmerHandler(SnowBallStemmerLanguageEnum[language.name])
        self._ner = SpacyNERHandler(SpacyLanguageEnum[language.name])
        self._spacy = GetSpacy(SpacyLanguageEnum[language.name])

    def Handle(self, sentence) -> SentenceFullAnalysysModel:
        out = SentenceFullAnalysysModel()

        document = self._spacy(sentence)
        start_search = 0
        for token in document:
            token_out = SentenceAnalysisModel()
            token_out.text = token.text
            token_out.language = token.lang_
            token_out.start = sentence.index(token.text, start_search)
            token_out.end = token_out.start + len(token.text)
            start_search = token_out.end     
            token_out.start_sentence = token.is_sent_start
            token_out.end_sentence = token.is_sent_end
            token_out.pos = POSTypeEnum[token.pos_]
            token_out.lemma = token.lemma_
            token_out.corrected_text = self._corrector.Handle(token.text)
            token_out.stem = self._stemmer.Handle(token.text)
            token_out.morphological = token.morph.to_dict()
            token_out.shape = token.shape_
            if(token.is_currency):
                token_out.text_type = TextTypeEnum.currency
            elif(token.is_punct):
                token_out.text_type = TextTypeEnum.punctuation
            elif(token.is_digit):
                token_out.text_type = TextTypeEnum.number
            else:
                token_out.text_type = TextTypeEnum.string
            token_out.is_stopword = False 
            
            out.sentence_analysis.append(token_out)

        out.ner = self._ner.NamedEntityRecognition(sentence)    

        return out 