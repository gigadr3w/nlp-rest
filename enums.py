from enum import Enum

class Languages(Enum):
    IT = "it"
    FR = "fr"
    EN = "en"
    ES = "es"
    DE = "de"

SpacyDictionaries = [(Languages.IT.value, "it_core_news_sm"),(Languages.EN.value, "en_core_web_sm"),(Languages.FR.value, "fr_core_news_sm"),(Languages.DE.value, "de_core_news_sm"), (Languages.ES.value, "es_core_news_sm")]
EnchantLanguages = [(Languages.IT.value, "it-IT"),(Languages.EN.value, "en-EN"),(Languages.FR.value, "fr-FR"),(Languages.DE.value, "de-DE"), (Languages.ES.value, "es-ES")]
SnowballStemmerLanguages = [(Languages.IT.value, "italian"),(Languages.EN.value, "english"),(Languages.FR.value, "french"),(Languages.DE.value, "german"), (Languages.ES.value, "spanish")]