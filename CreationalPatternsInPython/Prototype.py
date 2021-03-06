# '''
# Credit: Darinka Zobenica ,
# '''


# To Address the Dependencies and Data Hazard issues we use Prototype design pattern.
# To overcome RAW , WAR, WAW issues prototype model created duplicate or clone an object.
# Class initialization needs to digest a lot of resources, including data, hardware resources, etc. These consumption can be avoided through prototype copy.
# An object generated by new needs very complicated data preparation or permission, so prototype pattern can be used.
# When an object needs to be accessed by other objects, and each caller may need to modify its value,
# we can consider using prototype mode to copy multiple objects for the use of callers, that is, protective copy.


# Implementation Steps:
# 1) Implement clonable interface.
# 2) Override the clone method in the object class.
# All objects that are copyable must implement a method called clone and use it to return exact copies of themselves.

from copy import deepcopy


class Prototype(object): # Create a prototype class
    def clone(self):      # Create clone method
        pass

class OtherClass(Prototype):  # Taking Prototype as parameter (Inheritance)
    def __init__(self , student1 , student2):
        self.student1 = student1
        self.student2 = student2

    def __operation__(self):              # Condition for operation
        self.performed_operation = True

    # def clone(self):   # cloning the object Method 1
    #     return deepcopy(self)

    def clone(self):     # Cloning the object Method 2
        obj = OtherClass(self.student1 , self.student2)
        obj.performed_operation = self.performed_operation
        return obj


if __name__ == "__main__":
    school1 = Prototype()
    print(school1)

    school2 = OtherClass("Ram" , "Shyam")
    print(school2)