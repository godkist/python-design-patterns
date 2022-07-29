from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def implement_feature_a(self) -> None:
        pass

    @abstractmethod
    def implement_feature_b(self) -> None:
        pass

    @abstractmethod
    def implement_feature_c(self) -> None:
        pass


class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self._product = Product()

    def reset(self) -> None:
        self._product = Product()

    @property
    def product(self) -> Product:
        product = self._product
        self.reset()
        return product

    def implement_feature_a(self) -> None:
        self._product.add('Feature A')

    def implement_feature_b(self) -> None:
        self._product.add('Feature B')

    def implement_feature_c(self) -> None:
        self._product.add('Feature C')


class Product:
    def __init__(self) -> None:
        self.features = []

    def add(self, feature: Any) -> None:
        self.features.append(feature)

    def list_features(self) -> None:
        print(f"Product features: {', '.join(self.features)}", end='')


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_minimal_viable_product(self) -> None:
        self.builder.implement_feature_a()

    def build_full_featured_product(self) -> None:
        self.builder.implement_feature_a()
        self.builder.implement_feature_b()
        self.builder.implement_feature_c()


if __name__ == '__main__':
    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder

    print('--- Standard basic product: ')
    director.build_minimal_viable_product()
    builder.product.list_features()

    print('\n')

    print('--- Standard full featured product: ')
    director.build_full_featured_product()
    builder.product.list_features()

    print('\n')

    print('--- Custom product: ')
    builder.implement_feature_a()
    builder.implement_feature_b()
    builder.product.list_features()
