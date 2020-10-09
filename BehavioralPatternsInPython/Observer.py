'''
Credit:
seanwasere ytbe
'''


# The Observer design pattern  in which the object , called a observable or the subject ,manage a list of dependents , called observers , and notifies them automatically of any internal state changes, and calls one of there methods.

# Analogy : Subscription of service.

from abc import ABCMeta, abstractmethod  # Abstract base class

class Main_Observerable(metaclass=ABCMeta):          # Meta class for Observable

    @staticmethod
    @abstractmethod
    def subscribe(observer):
        """ This is the subscribe Method """

    @abstractmethod
    def unSubscribe(observer):
        """ This is UnSubscribe Method"""

    @abstractmethod
    def notify(observer):
        """ This is the Notifier Method"""

class Subject(Main_Observerable):
    def __init__(self):
        self._observer = set()

    def subscribe(self, observer):
        self._observer.add(observer)

    def unSubscribe(self , observer):
        self._observer.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observer:
            observer.notify(self, *args, **kwargs)


class Main_Observer(metaclass=ABCMeta):        # Meta class for Observer

    def __init__(self , name):
        self.name = name

    @staticmethod
    @abstractmethod
    def notify(observable, *args, **kwargs):
        """Receiver notifications"""

class Observer(Main_Observer):                         #class to implement Main_observer interface

    def __init__(self , observable , name):
        self.name = name
        observable.subscribe(self)


    def  notify(self, observable , *args , **kwargs):
        print("observer", self.name," received" , args , kwargs)


if __name__ == "__main__":

    SUBJECT = Subject()
    observer1 = Observer(SUBJECT , "Observer1")
    observer2 = Observer(SUBJECT , "Observer2")
    observer3 = Observer(SUBJECT, "Observer3")
    SUBJECT.notify("Got Observers" , [1,2,3] , {"a" : 1 , "b" : 2})


