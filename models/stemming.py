class StemmingModel():
    def __init__(self) -> None:
        self._s = list()
    @property 
    def Sentences(self) -> list:
        return self._s
    @Sentences.setter
    def Setter(self, value: list):
        self._s = value
