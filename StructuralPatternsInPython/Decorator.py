
# The Decorator Pattern is used to add functionality to a class without changing the class itself

# analogy : Fruits and vegetables

from abc import ABC , abstractmethod

class FruitsAndVegetables(ABC):   # Abstract class

    @abstractmethod
    def get_handle(self , c):
        pass

class Fruits:                         # Base Class
    def __init__(self):
        pass

    def get_handle(self , c):
        if c == "a":
            print('Apple')
        elif c == "b":
            print('Banana')
        elif c == "c":
            print("Cherries")
        else:
            print("not defined")

class Vegetables1(FruitsAndVegetables):       # Wrapper class or Decorator
    def __init__(self,wrapper):
        self.wrapper = wrapper

    def get_handle(self , c):
        if c == "a":
            print("Asparagus" ,  end=' , ')

        self.wrapper.get_handle(c)

class Vegetables2(FruitsAndVegetables):      # Wrapper class or Decorator
    def __init__(self,wrapper):
        self.wrapper = wrapper

    def get_handle(self , c):
        if c == "a":
            print("Asian_greens" ,  end=' , ')

        self.wrapper.get_handle(c)

if __name__ == "__main__":

    fruits = Fruits()

    fruits.get_handle("a")
    fruits.get_handle("b")

    fruits = Vegetables1(fruits)
    fruits.get_handle("a")


    fruits = Vegetables2(fruits)
    fruits.get_handle("a")




