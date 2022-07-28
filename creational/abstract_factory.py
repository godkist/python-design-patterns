from __future__ import annotations
from abc import ABC, abstractmethod


'''
    Factory 
'''


class SmartPhoneFactory(ABC):
    @abstractmethod
    def create_ap(self, battery: Battery) -> AP:
        pass

    @abstractmethod
    def create_battery(self) -> Battery:
        pass


class GalaxyFactory(SmartPhoneFactory):
    def create_ap(self, battery: Battery) -> AP:
        return GalaxyAP(battery)

    def create_battery(self) -> Battery:
        return SamsungBattery()


class IPhoneFactory(SmartPhoneFactory):
    def create_ap(self, battery: Battery) -> AP:
        return IPhoneAP(battery)

    def create_battery(self) -> Battery:
        return AppleBattery()


'''
    AP
'''


class AP(ABC):
    @abstractmethod
    def process(self) -> None:
        pass

    @abstractmethod
    def _active(self) -> None:
        pass


class GalaxyAP(AP):
    def __init__(self, battery: Battery):
        self.battery = battery

    def process(self) -> None:
        if 1 < self.battery.get_power():
            self._active()
        else:
            print('A battery runs out')

    def _active(self) -> None:
        print('The GalaxyAP is acting up')


class IPhoneAP(AP):
    def __init__(self, battery: Battery):
        self.battery = battery

    def process(self) -> None:
        if 2 < self.battery.get_power():
            self._active()
        else:
            print('A battery runs out')

    def _active(self) -> None:
        print('The IPhoneAP is acting up')


'''
    Battery
'''


class Battery(ABC):
    @abstractmethod
    def get_power(self) -> int:
        pass


class SamsungBattery(Battery):
    def get_power(self) -> int:
        return 2


class AppleBattery(Battery):
    def get_power(self) -> int:
        return 2


'''
    Client
'''


def client_code(factory: SmartPhoneFactory) -> None:
    battery = factory.create_battery()
    ap = factory.create_ap(battery)
    ap.process()


if __name__ == '__main__':
    print('--- assembling galaxy phone ---')
    client_code(GalaxyFactory())
    print('--- assembling apple phone ---')
    client_code(IPhoneFactory())
