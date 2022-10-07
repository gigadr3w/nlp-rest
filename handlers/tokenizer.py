from nltk import word_tokenize, sent_tokenize

class TokenizerHandler():
    def GetWords(sentence:str) -> list():
        '''Get the list of words contained in the sentence'''
        return word_tokenize(sentence)
    def GetStatements(sentences:str) -> list():
        '''Get the list of sentences contained in the main sentence'''
        return sent_tokenize(sentences)

