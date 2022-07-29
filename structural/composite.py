from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Media(ABC):
    @property
    def parent(self) -> Media:
        return self._parent

    @parent.setter
    def parent(self, parent: Media):
        self._parent = parent

    def add(self, component: Media) -> None:
        pass

    def remove(self, component: Media) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def play(self) -> str:
        pass


class Movie(Media):
    def __init__(self, title: str):
        self._title = title

    def play(self) -> str:
        return f'(Movie playing: {self._title})'


class PlayList(Media):
    def __init__(self) -> None:
        self._children: List[Media] = []

    def add(self, component: Media) -> None:
        self._children.append(component)
        component.parent = self

    def remove(self, component: Media) -> None:
        self._children.remove(component)
        component.parent = None

    def is_composite(self) -> bool:
        return True

    def play(self) -> str:
        results = []
        for child in self._children:
            results.append(child.play())
        return f"PlayList({' -> '.join(results)})"


def client_code(media: Media) -> None:
    print(f'RESULT: {media.play()}')


def client_code2(playlist: Media, movie: Media) -> None:
    if playlist.is_composite():
        playlist.add(movie)
    print(f'RESULT: {playlist.play()}')


if __name__ == '__main__':
    print('--- play')
    movie = Movie('The Dark Knight')
    client_code(movie)

    print('--- play')
    playlists = PlayList()
    playlist1 = PlayList()
    playlist1.add(Movie('Inception'))
    playlist1.add(Movie('The Matrix'))
    playlist2 = PlayList()
    playlist2.add(Movie('The Godfather'))
    playlists.add(playlist1)
    playlists.add(playlist2)
    client_code(playlists)

    print('--- play')
    client_code2(playlists, movie)
