from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class TurnOnCommand(Command):
    def __init__(self, receiver: LightReceiver) -> None:
        self._receiver = receiver

    def execute(self) -> None:
        self._receiver.turn_on()


class TurnOffCommand(Command):
    def __init__(self, receiver: LightReceiver) -> None:
        self._receiver = receiver

    def execute(self) -> None:
        self._receiver.turn_off()


class LightReceiver:
    def turn_on(self) -> None:
        print(f'Receiver: Light turn on')

    def turn_off(self) -> None:
        print(f'Receiver: Light turn off')


class Invoker:
    def __init__(self, on_start: Command, on_finish: Command):
        self._on_start = on_start
        self._on_finish = on_finish

    def visit(self) -> None:
        print("--- Invoker: visiting")
        if isinstance(self._on_start, Command):
            self._on_start.execute()
        if isinstance(self._on_finish, Command):
            self._on_finish.execute()
        print("--- Invoker: bye")


if __name__ == "__main__":
    receiver = LightReceiver()

    invoker = Invoker(
        TurnOnCommand(receiver),
        TurnOffCommand(receiver)
    )
    invoker.visit()
