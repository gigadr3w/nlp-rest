class TokenizationModel():
    def __init__(self) -> None:
        self._sentence = str()
        self._tokens = list()

    @property 
    def sentence(self):
        return self._sentence
    @sentence.setter
    def sentence(self, value):
        self._sentence = value
        
    @property
    def tokens(self) -> list:
        return self._t
    @tokens.setter
    def tokens(self,value: list):
        self._t = value
