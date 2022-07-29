from __future__ import annotations
from abc import ABC, abstractmethod


class Switch:
    def __init__(self, appliance: Appliance) -> None:
        self.appliance = appliance

    def turn_on(self) -> str:
        return f'Switch: {self.appliance.run()}'


class RemoteControl(Switch):
    def turn_on(self) -> str:
        return f'RemoteControl: {self.appliance.run()}'


class Appliance(ABC):
    @abstractmethod
    def run(self) -> str:
        pass


class TV(Appliance):
    def run(self) -> str:
        return 'TV turned on'


class VacuumCleaner(Appliance):
    def run(self) -> str:
        return 'VacuumCleaner turned on'


def client_code(switch: Switch) -> None:
    print(switch.turn_on())


if __name__ == "__main__":
    tv = TV()
    control = RemoteControl(tv)
    client_code(control)

    vc = VacuumCleaner()
    switch = Switch(vc)
    client_code(switch)
