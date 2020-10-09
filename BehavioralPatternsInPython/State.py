'''
Credit:

'''

# The State pattern is closely related to the concept of a Finite-State Machine.
# In state design pattern the class behavour changes as per its state
# In State Design pattern , there is a object representing various states and the context object whose behavour varies as its state object change


# Implementation Steps:
#
# Create and interface
# Create a concrete class implementing the same interface
# Create context class
# Use the context to see change in the behavour when state changes

# Analogy  lightsOn and lightsOff

import time
from abc import ABCMeta, abstractmethod


# Create and interface

class State(metaclass=ABCMeta):

    @abstractmethod
    def state_change(self):
        pass


# Create a concrete class implementing the same interface

class LightOn(State):
    def state_change(self):
        print("Switching On the Light")


class LightOff(State):
    def state_change(self):
        print("Switching Off the Light")


# Create context class

class ContextClass(State):
    def __init__(self):
        self.CurState = None  # Setting the initial state to None

    def set_state(self, CurState):         # Set the state
        self.CurState = CurState

    def state_change(self):
        print(time.time())                                          # record time between switch on and off
        self.CurState.state_change()                            # State change




if __name__ == "__main__":

    set_context = ContextClass()

    Onstate = LightOn()
    Offstate = LightOff()
    set_context.set_state(Onstate)
    set_context.state_change()
    time.sleep(5)
    set_context.set_state(Offstate)
    set_context.state_change()
    time.sleep(5)
    set_context.set_state(Onstate)
    set_context.state_change()
    time.sleep(5)
    set_context.set_state(Offstate)
    set_context.state_change()



