from ast import Param
from symbol import parameters


class TokenizationModel():
    def __init__(self) -> None:
        self._ = list()
    @property
    def tokens(self) -> list:
        return self._t
    @tokens.setter
    def tokens(self,value: list):
        self._t = value
