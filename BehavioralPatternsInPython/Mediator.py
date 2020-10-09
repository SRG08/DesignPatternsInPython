'''
Credits:
seanwasere ytbe
'''

# With the mediator pattern communication between the objects are encapsulated within a mediator object.
# Objects communicate with each other rather than communicating directly with each other.

# Analogy: Bulk Message notification


from abc import ABCMeta , abstractmethod

class Meta_component(metaclass=ABCMeta):    # Meta Class

    @abstractmethod
    def notify(msg):
        """ This Required notify Method"""

    @abstractmethod
    def receiver(msg):
        """ This requires receiver method"""

class Component(Meta_component):
    def __init__(self, mediator , name):
        self.mediator = mediator
        self.name = name

    def notify(self , message):
        print(self.name +" : >>> OUT >>> :" + message)
        self.mediator.notify(message , self)

    def receiver(self, message):
        print(self.name + " : <<< IN <<< :" + message)




class Mediator():

    def __init__(self):
        self.Components = []


    def add(self, component):
        self.Components.append(component)

    def notify(self,message , component):
        for _component in self.Components:
            if _component != component:
                _component.receiver(message)



if __name__ == "__main__":

    MEDIATOR = Mediator()

    COMPONENT1 = Component(MEDIATOR, "Component1")
    COMPONENT2 = Component(MEDIATOR, "Component2")
    COMPONENT3 = Component(MEDIATOR, "Component3")

    MEDIATOR.add(COMPONENT1)
    MEDIATOR.add(COMPONENT2)
    MEDIATOR.add(COMPONENT3)

    COMPONENT1.notify("data")

