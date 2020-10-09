'''
Credits:
seanwasere ytbe
'''

# This pattern is used to get a way to access the elements of a collection object in sequential manner
# without any need to know its underlying representation.

# Analogy : Counting of tokens

from abc import ABCMeta , abstractmethod

class Interface_Iterator(metaclass=ABCMeta):   # Meta Class

    @abstractmethod
    def next(self):
        """ Returns the next method of the iterator"""

    @abstractmethod
    def has_next(self):
        """ returns the has_next of the iterator"""

class Iterable(Interface_Iterator):

    def __init__(self):
        self.index = 0
        self.number = 5

    def next(self):
        if self.index < self.number:
            iter = self.index
            self.index += 1
            return iter
        else:
            return Exception("There is no next in the iter")

    def has_next(self):
        return self.index < self.number

#Client:
if __name__ == "__main__" :
    iterator = Iterable()         # Creating object
    print(iterator.next())         # Iter 0
    print(iterator.next())          # Iter 1
    print(iterator.next())          # Iter 2
    print(iterator.next())          # Iter 3



