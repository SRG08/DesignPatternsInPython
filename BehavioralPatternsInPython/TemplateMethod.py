'''
Credit:

'''

from abc import ABCMeta , abstractmethod

class Abstract_Template(metaclass=ABCMeta):


    @abstractmethod
    def Morning(self):
        """ This is Morning Abstract Method"""

    @abstractmethod
    def Afternoon(self):
        """ This is Afternoon Abstract Method"""

    @abstractmethod
    def Evening(self):
        """ This is Evening Abstract Method"""

    def execute(self):
        self.Morning()
        self.Afternoon()
        self.Evening()


class Weekdays(Abstract_Template):
    def __init__(self):
        pass

    def Morning(self):
        print("Weekdays : Get up at 4'o Clock and Go to Office at 9'0 clock")

    def Afternoon(self):
        print("Weekdays : Work till 1'o Clock , Have Lunch , Start working at 2'o Clock")


    def Evening(self):
        print("Weekdays : Log Out at 6'o Clock, Go Home have Dinner at 8'o Clock and Sleep\n")
        print("*"*50 + '\n')


class Weekends(Abstract_Template):
    def __init__(self):
        pass

    def Morning(self):
        print("Weekends : Have breakfast and Sleep")

    def Afternoon(self):
        print("Weekends : Have Lunch at 1'o Clock and Sleep ")


    def Evening(self):
        print("Weekends : Have Dinner at 8'o Clock and Sleep\n")


if __name__ == "__main__":
    Weekday = Weekdays()
    Weekday.execute()

    Weekend = Weekends()
    Weekend.execute()