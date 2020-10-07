# '''
# Credit: Robley Gori
# '''

# Singleton is a Creational design pattern where it ensure that a class has only one instance
# It ensures to provide global access point to across all classes and modules
# The simplest example is "with open(xyz.txt, 'wb') as file:" code. Modules are “singletons” as import creates same object of the class and not the new object.
# Singleton is as called as one-element tuple ,  Logger is an example of singleton Example given below.


# Implementation Steps:
# 1) The class of Singleton design pattern is restricted to only one object.
# 2) Create the object in a @staticmethod to control the object creation instance of the class.
# 3) all calls made to the object of the class either returns the original singleton object.

class Singleton_life:   # Creating Singleton class
    __instance__ = None  # defining Instance is None

    def __init__(self): # Constructor
        # self.value = value
        if Singleton_life.__instance__ is None:  # Checking if instance is created
            Singleton_life.__instance__ = self # Storing instance in single point of memory
        else:
            raise Exception("Singleton Object cannot be created")  # Raise exception if instance is created

    @staticmethod   # Creating Static method of the class
    def sameLife():
        if not Singleton_life.__instance__:  # If Instance is not created
            Singleton_life()                  # Function Call to create instance
            return  Singleton_life.__instance__  # Returning the instance



# another way to implement singleton Method 2:
print("*"*50)

class Singletons(object):
    __instance__ = None  # Making the instance private so that the other class could not access the instance

    def __new__(self):
        if not self.__instance__:  # If instance not present  then create one
            self.__instance__= super(Singletons, self).__new__(self)  # Instance created
            self.x = 50
            return self.__instance__  # return instance

if __name__ == "__main__":
    life = Singleton_life()   # Singleton Object Created
    print(life)

    learning_life = Singleton_life.sameLife() # sameLife instance assigned to object
    print(learning_life)

    enjoying_life  = Singleton_life.sameLife() # sameLife instance assigned to object
    print(enjoying_life)

    # another_life = Singleton_life()  # Singleton Object Cannot be Created , Uncomment and check
    # print(another_life)



    y = Singletons()
    print(y.x)

    other = Singletons()
    print(other.y)

