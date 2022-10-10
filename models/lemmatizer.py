class LemmatizerModel():
    def __init__(self) -> None:
        self._s = list()        
    @property 
    def sentences(self) -> list:
        return self._s
    @sentences.setter
    def Setter(self, value: list):
        self._s = value
