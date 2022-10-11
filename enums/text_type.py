import enum
from locale import currency
from string import punctuation

class TextTypeEnum(enum.Enum):
    string='string'
    punctuation='punctuation'
    number='number'
    email='email'
    url='url'
    currency='currency'