'''
Cridit:
K.S.Srivastava
'''


# The Memento pattern delegates creating the state snapshots to the actual owner of that state, the originator object
# Hence, instead of other objects trying to copy the editor’s state from the
# “outside,” the editor class itself can make the snapshot since it has full access to its own state.

# Analogy : Restoring Previous state UNDO Operation


class Memento:
    def __init__(self, value):
        self.state = value

    def SetState(self, value):
        self.state = value

    def GetState(self):
        return self.state

class Originator:

    def SetState(self, value):
        self.state = value

    def GetState(self):
        return self.state

    def CreateMemento(self):
        return (Memento(self.state))

    def SetMemento(self , memento):
        print("Going to previous state")
        self.state = memento.GetState()

class Caretaker:
    def __init__(self, originatorObj):
        self.memento = None
        self.origin = originatorObj

    def Execute(self):
        self.memento = self.origin.CreateMemento()
        self.origin.SetState(0)

    def Unexecute(self):
        self.origin.SetMemento(self.memento)

if __name__ == "__main__":

    originator = Originator()

    originator.SetState(1)
    print("The state value is :" ,  originator.GetState())


    caretaker = Caretaker(originator)
    caretaker.Execute()
    print("The state value is :" , originator.GetState())

    caretaker.Unexecute()
    print("The state value is :" , originator.GetState())


