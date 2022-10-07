from ast import Param
from symbol import parameters


class TokenizationModel():
    def __init__(self) -> None:
        self._ = str()
    @property
    def Token(self):
        return self._t
    @Token.setter
    def Token(self,value):
        self._t = value
