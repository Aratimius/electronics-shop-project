from src.item import Item


class MixinLog:

    def __init__(self):
        # Язык по умолчанию английский
        self._language = 'EN'

    def change_lang(self):
        """Смена языка"""
        if self._language == 'EN':
            self._language = 'RU'
        elif self._language == 'RU':
            self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, lang):
        """Если при присваивании язык будет не RU или EN, то выскочит ошибка AttributeError"""
        if lang not in ['RU', 'EN']:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        else:
            self._language = lang


class Keyboard(Item, MixinLog):
    pass

print(Keyboard.__mro__)