
class Component:
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    def operation(self) -> str:
        return 'ConcreteComponent'


class Decorator(Component):
    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f'ConcreteDecoratorA({self.component.operation()})'


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f'ConcreteDecoratorB({self.component.operation()})'


def client_code(component: Component) -> None:
    print(f'> {component.operation()}')


if __name__ == '__main__':
    print("--- simple component")
    simple = ConcreteComponent()
    client_code(simple)

    print("--- decorated component")
    decorator1 = ConcreteDecoratorA(simple)
    decorator2 = ConcreteDecoratorB(decorator1)
    client_code(decorator2)
