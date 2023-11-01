#!/usr/bin/python3

from abc import ABC, abstractmethod

class EventListener(ABC):
    @abstractmethod
    def update(self, message):
        pass

class Subject:
    def __init__(self):
        self.subscribers = []

    def attach(self, subscriber: EventListener):
        self.subscribers.append(subscriber)
    
    def notify(self, message: str):
        for subscriber in self.subscribers:
            subscriber.update(message)

class Observer(EventListener):
    def __init__(self):
        self.notification = "Empty"
    
    def update(self, message):
        self.notification = message
        print(self.notification)

class SecondObserver(EventListener):
    def __init__(self):
        self.notification = "Empty"

    def update(self, message):
        self.notification = message + " in second observer"
        print(self.notification)
    

subject = Subject()
observer1 = Observer()
observer2 = SecondObserver()
subject.attach(observer1)
subject.attach(observer2)
print("--Evento--")
subject.notify("Evento importante")
print("--Evento--")
subject.notify("Eres ganador de 1000USD. Entra al siguiente link para reclamar tu premio:...")
