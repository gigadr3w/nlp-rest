class CorrectionModel():
    def __init__(self) -> None:
        self._s = list()

    @property
    def sentences(self):
        return self._s
    @sentences.setter
    def sentences(self, value):
        self._s = value