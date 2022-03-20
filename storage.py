from abc import ABC, abstractmethod

class Storage (ABC):

    @abstractmethod
    def add(self, name, quantity):
        pass

    @abstractmethod
    def remove(self, name, quantity):
        pass

    # `remove`( < название >, < количество >) - уменьшает
    # запас
    # items

    @abstractmethod
    def _get_free_space(self):
        pass

    # `get_free_space()` - вернуть
    # количество
    # свободных
    # мест

    @abstractmethod
    def _get_items(self):
        pass

    # `get_items()` - возвращает
    # сожержание
    # склада
    # в
    # словаре
    # {товар: количество}

    @abstractmethod
    def _get_unique_items_count(self):
        pass

    # `get_unique_items_count()` - возвращает
    # количество
    # уникальных
    # товаров.

