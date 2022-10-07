from ast import Param
from symbol import parameters


class TokenizationModel():
    def __init__(self) -> None:
        self._t = list()
    @property
    def Tokens(self):
        return self._t
    @Tokens.setter
    def Tokens(self,value):
        self._t = value
