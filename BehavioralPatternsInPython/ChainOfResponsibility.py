'''
credit :
seanwasere ytbe
'''




# Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers.
# Chain of Responsibility, Command, Mediator, and Observer, address how you can decouple senders and receivers, but with different trade-offs.
# Chain of Responsibility passes a sender request along a chain of potential receivers.
# Chain of Responsibility can use Command to represent requests as objects.
# Chain of Responsibility is often applied in conjunction with Composite. There, a component's parent can act as its successor.


# Implementation steps:

# The base class maintains a "next" pointer.
# Each derived class implements its contribution for handling the request.
# If the request needs to be "passed on", then the derived class "calls back" to the base class, which delegates to the "next" pointer.
# The client (or some third party) creates and links the chain (which may include a link from the last node to the root node).
# The client "launches and leaves" each request with the root of the chain.
# Recursive delegation produces the illusion of magic.


# Analogy : AMT Machine

from abc import ABCMeta, abstractmethod

class Initial_Handler(metaclass=ABCMeta):
    """ The interface for handling requests"""

    @abstractmethod
    def set_successor(successor):
        """set the next handle in the chain"""

    @abstractmethod
    def handle_event(amount):
        """ handles the event"""


class Dispenser50(Initial_Handler):

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        """ Set the Successor"""
        self._successor = successor

    def handle_event(self, amount):
        """ Dispense Rs 50 notes of applicable, otherwise continues to successor"""
        self.amount = amount
        if amount >=50:
            num = amount//50
            remainder = amount % 50
            print(f"Dispensing {num} Rs50 Notes")
            if remainder !=0:
                self._successor.handle_event(remainder)
        else:
            self._successor.handle_event(amount)


class Dispenser20(Initial_Handler):

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        """ Set the Successor"""
        self._successor = successor

    def handle_event(self, amount):
        """ Dispense Rs 20 notes of applicable, otherwise continues to successor"""
        self.amount = amount
        if amount >=20:
            num = amount//20
            remainder = amount % 20
            print(f"Dispensing {num} Rs20 Notes")
            if remainder !=0:
                self._successor.handle_event(remainder)
        else:
            self._successor.handle_event(amount)


class Dispenser10(Initial_Handler):

    def __init__(self):
        self._successor = None

    def set_successor(self, successor):
        """ Set the Successor"""
        self._successor = successor

    def handle_event(self, amount):
        """ Dispense Rs 10 notes of applicable, otherwise continues to successor"""
        self.amount = amount
        if amount >=10:
            num = amount//10
            remainder = amount % 10
            print(f"Dispensing {num} Rs10 Notes")
            if remainder !=0:
                self._successor.handle_event(remainder)
        else:
            self._successor.handle_event(amount)


class ATMDispenserChainOfResponsibility:
    """ The Chain Client"""
    def __init__(self):
        self.chain1 = Dispenser50()
        self.chain2 = Dispenser20()
        self.chain3 = Dispenser10()

        """ Set the chain of responsibility
        the handler can also set it dynamically at handletime"""

        self.chain1.set_successor(self.chain2)
        self.chain2.set_successor(self.chain3)


if __name__ == "__main__":
    ATM = ATMDispenserChainOfResponsibility()

    Amount = int(input("please input the amount :"))
    if Amount < 10 or Amount % 10 != 0:
        print("Enter a positive amount and Multiples of 10s")
        exit()
    ATM.chain1.handle_event(Amount)