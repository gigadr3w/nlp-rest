from os import stat
from symbol import star_expr


class NamedEntityRecognitionModel():
    def __init__(self) -> None:
        self._text = str()
        self._start = 0
        self._end = 0
        self._entity = str()

    @property
    def text(self):
        return self._text
    @text.setter
    def text(self, value):
        self._text = value

    @property
    def start(self):
        return self._start
    @start.setter
    def start(self, value):
        self._start = value

    @property
    def end(self):
        return self._end
    @end.setter
    def end(self, value):
        self._end = value

    @property
    def entity(self):
        return self._entity
    @entity.setter
    def entity(self, value):
        self._entity = value