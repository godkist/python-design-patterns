from __future__ import annotations
from abc import ABC, abstractmethod


'''
    Creator
'''


class Creator(ABC):
    @abstractmethod
    def create_shape(self):
        pass

    def render(self) -> str:
        pencil = self.create_shape()
        return pencil.draw()


class ConcreteCreator1(Creator):
    def create_shape(self) -> Shape:
        return Circle()


class ConcreteCreator2(Creator):
    def create_shape(self) -> Shape:
        return Rectangle()


'''
    Pencil
'''


class Shape(ABC):
    @abstractmethod
    def draw(self) -> str:
        pass


class Circle(Shape):
    def draw(self) -> str:
        return 'circle'


class Rectangle(Shape):
    def draw(self) -> str:
        return 'rectangle'


def client_code(creator: Creator) -> None:
    print(creator.render())


if __name__ == '__main__':
    print('--- with the ConcreteCreator1')
    client_code(ConcreteCreator1())
    print('--- with the ConcreteCreator2')
    client_code(ConcreteCreator2())
