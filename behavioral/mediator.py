from __future__ import annotations
from abc import ABC, abstractmethod


class Colleague(ABC):
    @abstractmethod
    def send(self, msg: str):
        pass

    @abstractmethod
    def receive(self, msg: str):
        pass


class ConcreteColleague(Colleague):
    def __init__(self, mediator, name):
        self._mediator = mediator
        self._name = name

    def send(self, msg: str):
        print(f'{self._name} sending message : {msg}')
        self._mediator.send_message(msg, self)

    def receive(self, msg: str):
        print(f'{self._name} receiving message : {msg}')


class Mediator(ABC):
    @abstractmethod
    def add_users(self, user):
        pass

    @abstractmethod
    def delete_user(self, user):
        pass

    @abstractmethod
    def send_message(self, msg:str, user):
        pass


class ConcreteMediator(Mediator):
    def __init__(self):
        self._users = []

    def add_users(self, *users):
        self._users.extend(users)

    def delete_user(self, user):
        self._users.remove(user)

    def send_message(self, msg: str, user):
        for _user in self._users:
            if _user == user:
                continue
            _user.receive(msg)


mediator = ConcreteMediator()
user1 = ConcreteColleague(mediator, 'lee')
user2 = ConcreteColleague(mediator, 'kim')
user3 = ConcreteColleague(mediator, 'park')
user4 = ConcreteColleague(mediator, 'yon')

mediator.add_users(user1, user2, user3, user4)
user1.send("hi")
mediator.delete_user(user4)
user2.send("hello")
