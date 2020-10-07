'''
Credit:
www.SourceMaking.com
seanwasere ytbe
'''

# Rules of thumb
# Chain of Responsibility, Command, Mediator, and Observer, address how you can decouple senders and receivers, but with different trade-offs.
# Command normally specifies a sender-receiver connection with a subclass.
# Chain of Responsibility can use Command to represent requests as objects.
# Command and Memento act as magic tokens to be passed around and invoked at a later time.
# In Command, the token represents a request; in Memento, it represents the internal state of an object at a particular time.
# Polymorphism is important to Command, but not to Memento because its interface is so narrow that a memento can only be passed as a value.
# Command can use Memento to maintain the state required for an undo operation.
# MacroCommands can be implemented with Composite.
# A Command that must be copied before being placed on a history list acts as a Prototype.
# Two important aspects of the Command pattern: interface separation (the invoker is isolated from the receiver), time separation (stores a ready-to-go processing request that's to be stated later).


# Analogy: Switching the lights ON or Off

import time
from abc import ABCMeta , abstractmethod

class ICommand(metaclass=ABCMeta):

    @abstractmethod
    def execute(self):
        """This is method to execute the commands"""

    # @abstractmethod
    # def OffCommand(self):
    #     """This is a meta class method to on the lights"""

class  Light():

    def OnLight(self):
        print("The Light is On")

    def OffLight(self):
        print("The Light is Off")

class OnCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.OnLight()

class OffCommand(ICommand):
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.OffLight()

class Switch:
    """ the invoker class"""

    def __init__(self):
        self._commands = {}
        self._hisory =[]       # To check the history how much time it was on and off

    def register(self, command_name , command):
        self._commands[command_name] = command

    def execute(self, command_name):
        if command_name in self._commands:
           self._commands[command_name].execute()
           self._hisory.append({time.time(): command_name})
        else:
            print("command not found")

    @property
    def history(self):
        return self._hisory

# Client
if __name__ == "__main__":
    #Receiver
    LIGHT = Light()
    # print(LIGHT)

    # Commands
    SwitchOn = OnCommand(LIGHT)
    SwitchOff = OffCommand(LIGHT)

    # Invoker
    Switch = Switch()

    # Register Commands for the invoker
    Switch.register("ON", SwitchOn )
    Switch.register("OFF", SwitchOff )

    # Execute Command
    Switch.execute("ON")
    Switch.execute("OFF")

    print(Switch.history)







