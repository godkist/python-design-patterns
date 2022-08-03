from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any


class ReverseIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class WordsCollection(Iterable):
    def __init__(self, collection=None) -> None:
        if collection is None:
            collection = []
        self._collection = collection

    def __iter__(self) -> ReverseIterator:
        return ReverseIterator(self._collection)

    def get_reverse_iterator(self) -> ReverseIterator:
        return ReverseIterator(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == '__main__':
    words = WordsCollection()
    words.add_item('First')
    words.add_item('Second')
    words.add_item('Third')

    print('--- Straight traversal:')
    print('\n'.join(words))
    print('')

    print('--- Reverse traversal:')
    print('\n'.join(words.get_reverse_iterator()), end='')
